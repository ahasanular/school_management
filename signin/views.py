from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher
from students.serializers import StudentDetailsSerializer
from teachers.serializers import TeacherDetailsSerializer
from django.http import HttpResponseRedirect
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# end of import


def sign_in(request):
    return render(request, 'signIn.html')


def my_dashboard(request):
    return render(request, 'myDashboard.html')


def log_out(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('token') #key must be added
    response.delete_cookie('username') #key must be added
    response.delete_cookie('fullname') #key must be added
    response.delete_cookie('img') #key must be added
    response.delete_cookie('account_type') #key must be added
    return response


# sign in api

class SignInApi(CreateAPIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            if 'email' not in data or data['email'] == '':
                feedback = {'status': HTTP_400_BAD_REQUEST, 'message': "Email field Cannot be null"}
                return Response(feedback)

            if 'password' not in data or data['password'] == '':
                feedback = {'status': HTTP_400_BAD_REQUEST, 'message': "Password field Cannot be null"}
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
                feedback = {'status': HTTP_400_BAD_REQUEST, 'message': "No Account with this User"}
                return Response(feedback)
            elif not user.is_active:
                feedback = {'status': HTTP_400_BAD_REQUEST, 'message': "Active you Account first"}
                return Response(feedback)
            else:
                if not check_password(data['password'],user.password):
                    feedback = {'status': HTTP_401_UNAUTHORIZED, 'message': "Invalid Credentials"}
                    return Response(feedback)
                else:
                    student = Student.objects.filter(email=user.email).first()
                    teacher = Teacher.objects.filter(email=user.email).first()

                    if teacher:
                        user_object = teacher
                        account_type = 'Teacher'
                    elif student:
                        user_object = student
                        account_type = 'Student'

                    token = RefreshToken.for_user(user)

                    feedback = {}
                    feedback['status'] = HTTP_200_OK
                    feedback['user_name'] = user.username
                    feedback['full_name'] = user_object.full_name
                    feedback['account_type'] = account_type
                    feedback['img'] = str(user_object.img.url)
                    feedback['access'] = str(token.access_token)
                    feedback['refresh'] = str(token)
                    return Response(feedback)

        except Exception as ex:
            feedback = {'status': HTTP_400_BAD_REQUEST, 'message': str(ex)}
            return Response(feedback)


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
            feedback = {'message': str(ex), 'status': HTTP_400_BAD_REQUEST}
            return Response(feedback)

