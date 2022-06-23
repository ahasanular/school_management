from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher
from students.serializers import StudentDetailsSerializer
from teachers.serializers import TeacherDetailsSerializer

def SignIn(request):
    return render(request, 'signIn.html')

def myDashboard(request):
    return render(request, 'myDashboard.html')

from django.http import HttpResponseRedirect

def log_out(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('token') #key must be added
    response.delete_cookie('username') #key must be added
    response.delete_cookie('fullname') #key must be added
    response.delete_cookie('img') #key must be added
    response.delete_cookie('account_type') #key must be added
    return response


# sign in api
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework_simplejwt.tokens import RefreshToken

class SignInApi(CreateAPIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            if 'email' not in data or data['email'] == '':
                feedback = {}
                feedback['status'] = HTTP_400_BAD_REQUEST
                feedback['message'] = "Email field Cannot be null"
                return Response(feedback)

            if 'password' not in data or data['password'] == '':
                feedback = {}
                feedback['status'] = HTTP_400_BAD_REQUEST
                feedback['message'] = "Password field Cannot be null"
                return Response(feedback)

            from django.db.models import Q

            student = Student.objects.filter(Q(email=data['email']) | Q(phone=data['email'])).first()
            teacher = Teacher.objects.filter(Q(email=data['email']) | Q(phone=data['email'])).first()
            if student:
                person_obj = student
                account_type = 'Student'
                user = person_obj.user
            elif teacher:
                person_obj = teacher
                account_type = 'Teacher'
                user = person_obj.user
            else:
                user = User.objects.filter(username=data['email']).first()

            if not user or user == '':
                feedback = {}
                feedback['status'] = HTTP_400_BAD_REQUEST
                feedback['message'] = "No Account with this User"
                return Response(feedback)
            elif not user.is_active:
                feedback = {}
                feedback['status'] = HTTP_400_BAD_REQUEST
                feedback['message'] = "Active you Account first"
                return Response(feedback)
            else:
                if not check_password(data['password'],user.password):
                    feedback = {}
                    feedback['status'] = HTTP_401_UNAUTHORIZED
                    feedback['message'] = "Invalid Credentials"
                    return Response(feedback)
                else:
                    student = Student.objects.filter(email=user.email).first()
                    teacher = Teacher.objects.filter(email=user.email).first()

                    if teacher:
                        userObject = teacher
                        account_type = 'Teacher'
                    elif student:
                        userObject = student
                        account_type = 'Student'

                    token = RefreshToken.for_user(user)
                    feedback = {}
                    feedback['status']=HTTP_200_OK
                    feedback['user_name']=user.username
                    feedback['full_name']=userObject.full_name
                    feedback['account_type']=account_type
                    feedback['img']=str(userObject.img.url)
                    feedback['access']=str(token.access_token)
                    feedback['refresh']=str(token)
                    print(feedback)
                    return Response(feedback)

        except Exception as ex:
            feedback = {}
            feedback['status'] = HTTP_400_BAD_REQUEST
            feedback['message'] = str(ex)
            return Response(feedback)


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class MyDashboard(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, name):
        try:
            student = Student.objects.filter(full_name=name).first()
            teacher = Teacher.objects.filter(full_name=name).first()
            if student:
                data = StudentDetailsSerializer(student).data
                data['status'] = HTTP_200_OK
                return Response(data)
            elif teacher:
                data = TeacherDetailsSerializer(teacher).data
                data['status'] = HTTP_200_OK
                return Response(data)

        except Exception as ex:
            feedback = {}
            feedback['message'] = str(ex)
            feedback['status'] = HTTP_400_BAD_REQUEST
            return Response(feedback)

