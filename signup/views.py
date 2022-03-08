import secrets
from threading import Thread

from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher
from django.contrib.auth.models import User, Group



def signUp(request):
    return render(request, 'signUp.html')

def verification(request, account_type, email, otp):
    return render(request, 'verification.html')


#api

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_208_ALREADY_REPORTED
from django.contrib.auth.hashers import make_password
import json



#full function to send a mail with otp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to, subject, body):
    smtp_server='smtp.gmail.com'
    smtp_port='465'
    sender_email='projecttestmail8@gmail.com'
    sender_password='projectTesting'
    server = None
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.ehlo()  # Can be omitted
        server.login(sender_email, sender_password)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to
        msg['Subject'] = subject


        html = """\
        <html>
            <head></head>
            <body>
        """
        html += body
        """
            </body>
        </html>
        """
        msg.attach(MIMEText(html,'html'))
        server.sendmail(
            from_addr=sender_email,
            to_addrs=to,
            msg = msg.as_string())
        print("Mail Send")
    except Exception as ex:
        print(str(ex))
    finally:
        if server != None:
            server.quit()

def send_email_thread(to, subject, body):
    thread = Thread(target=send_email,args=(to, subject, body))
    thread.start()

class SignUp(CreateAPIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            print("data['full_name']")
            print(data['full_name'])
            if 'account_type' not in data or data['account_type'] == '':
                result = {}
                result['status'] = HTTP_400_BAD_REQUEST
                result['message'] = "No account type found !"
                return Response(result)
            if 'full_name' not in data or data['full_name'] == '':
                result = {}
                result['status'] = HTTP_400_BAD_REQUEST
                result['message'] = "Full name can't be NULL"
                return Response(result)
            if 'email' not in data or data['email'] == '':
                result = {}
                result['status'] = HTTP_400_BAD_REQUEST
                result['message'] = "Email can't be NULL"
                return Response(result)
            if 'phone' not in data or data['phone'] == '':
                result = {}
                result['status'] = HTTP_400_BAD_REQUEST
                result['message'] = "Phone can't be NULL"
                return Response(result)
            if 'password' not in data or data['password'] == '':
                result ={}
                result['status'] = HTTP_400_BAD_REQUEST
                result['message'] = "Password can't be NULL"
                return Response(result)

            username = data['email'].split('@')

            user = User.objects.filter(username=username[0]).first()

            if not user:
                user = User()
                user.username = username[0]
                name = data['full_name'].split(' ')
                user.first_name = name[0]
                user.last_name = name[1]
                user.email = data['email']
                user.password = make_password(data['password'])
                user.is_active = False



                otp = secrets.token_hex(50)

                print("PersonChecking")
                print(data['account_type'])

                if data['account_type'] == 'Student':
                    person_obj = Student()
                elif data['account_type'] == 'Teacher':
                    person_obj = Teacher()

                person_obj.user = user

                address = data['street'] + ", " + data['city'] + ", " + data['state'] + " - " + data['zip']

                person_obj.full_name = data['full_name']
                person_obj.fathers_name = data['fathers_name']
                person_obj.mothers_name = data['mothers_name']
                person_obj.gender = data['gender']
                person_obj.religion = data['religion']
                person_obj.birth_date = data['dob']
                person_obj.email = data['email']
                person_obj.phone = data['phone']
                person_obj.address = address
                person_obj.blood_group = data['blood_group']
                person_obj.otp = otp
                if 'profile_photo' not in data or data['profile_photo'] == '' or not request.FILES['profile_photo']:
                    result = {}
                    result['status'] = HTTP_400_BAD_REQUEST
                    result['message'] = "Photo Not found"
                    return Response(result)
                else:
                    person_obj.img = data['profile_photo']

                user.save()
                person_obj.save()

                server_root = "http://127.0.0.1:8000/sign_up/verification/" + data['account_type'] + "/"
                activition_link = server_root + data['email'] + "/" + otp + "/"

                send_email_thread(data['email'], "Verification for " + data['account_type'] + " Sign Up", "To confirm your mail and activate your account please click in this LINK : " + activition_link)

                result = {}
                result['status'] = HTTP_200_OK
                result['messege'] = "Success"
                return Response(result)
            else:
                if user.is_active:
                    feedback = {}
                    feedback['message'] = "An Account Exist with this Email !"
                    feedback['status'] = HTTP_208_ALREADY_REPORTED
                    return Response(feedback)
                else:
                    feedback = {}
                    feedback['message'] = "Un Active Account Found !"
                    feedback['status'] = HTTP_401_UNAUTHORIZED
                    return Response(feedback)

        except Exception as ex:
            result = {}
            result['message'] = str(ex)
            result['status'] = HTTP_400_BAD_REQUEST
            return Response(result)


class OtpCheck(CreateAPIView):
    permission_classes = []
    def put(self, request):
        try:
            data = json.loads(request.body)

            if 'account_type' not in data or data['account_type'] == '':
                feedback = {}
                feedback['status'] = HTTP_400_BAD_REQUEST
                feedback['message'] = "Account type not Found !"
                return Response(feedback)
            if 'otp' not in data or data['otp'] == '':
                feedback = {}
                feedback['status'] = HTTP_400_BAD_REQUEST
                feedback['message'] = "OTP cant be NULL"
                return Response(feedback)
            if 'otpEmail' not in data or data['otpEmail'] == '':
                feedback = {}
                feedback['status'] = HTTP_400_BAD_REQUEST
                feedback['message'] = "Email Lost : Something went wrong"
                return Response(feedback)

            user = User.objects.filter(email=data['otpEmail']).first()

            if not user or user == '':
                feedback = {}
                feedback['status'] = HTTP_400_BAD_REQUEST
                feedback['message'] = "Your Data is not on Database"
                return Response(feedback)
            if data['account_type'] == 'Student':
                person_obj = Student.objects.filter(user=user).first()
                group_type = 'Student_Group'
            elif data['account_type'] == 'Teacher':
                person_obj = Teacher.objects.filter(email=data['otpEmail']).first()
                group_type = 'Teacher_Group'

            if person_obj.email == data['otpEmail'] and person_obj.otp == data['otp']:
                user.is_active = True
                group = Group.objects.filter(name=group_type).first()
                user.groups.add(group)
                user.save()
                person_obj.otp = ''
                person_obj.save()

                feedback = {}
                feedback['status'] = HTTP_200_OK
                feedback['message'] = "Account Creation successful"
                return Response(feedback)

            else:
                feedback = {}
                feedback['status'] = HTTP_401_UNAUTHORIZED
                feedback['message'] = "UnAuthorized entry"
                return Response(feedback)


        except Exception as ex:
            feedback = {}
            feedback['status'] = HTTP_400_BAD_REQUEST
            feedback['message'] = str(ex)
            return Response(feedback)



class SendVerificationLink(CreateAPIView):
    permission_classes = []
    def post(self, request):
        try:
            data = json.loads(request.body)
            if 'email' not in data or data['email'] == '':
                feedback = {}
                feedback['message'] = "Email LOST ! Something Went Wrong"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)
            if 'account_type' not in data or data['account_type'] == '':
                feedback = {}
                feedback['message'] = "Account Type Is not Valid !"
                feedback['status'] = HTTP_400_BAD_REQUEST
                return Response(feedback)

            user = User.objects.filter(email=data['email'])
            otp = secrets.token_hex(20)
            server_root = "http://127.0.0.1:8000/sign_up/verification/" + data['account_type'] + "/"

            if user:
                student = Student.objects.filter(email=data['email']).first()
                print("student")
                print(student)
                teacher = Teacher.objects.filter(email=data['email']).first()
                print("teacher")
                print(teacher)
                if student:
                    student.otp = otp
                    student.save()
                elif teacher:
                    teacher.otp = otp
                    teacher.save()
                else:
                    feedback = {}
                    feedback['message'] = "Account Is not Valid !"
                    feedback['status'] = HTTP_400_BAD_REQUEST
                    return Response(feedback)

            activition_link = server_root + data['email'] + "/" + otp + "/"

            send_email(data['email'], "Verification for Sign Up", "To confirm your mail and activate your account please click in this LINK : " + activition_link)

            feedback = {}
            feedback['message'] = "Activation Mail Send !"
            feedback['status'] = HTTP_200_OK
            return Response(feedback)

        except Exception as ex:
            feedback = {}
            feedback['message'] = str(ex)
            feedback['status'] = HTTP_400_BAD_REQUEST
            return Response(feedback)