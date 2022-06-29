from django.shortcuts import render
from .models import Teacher
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import TeacherListSerializer, TeacherDetailsSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission
# end of import

# function based frontend view

# def teacherIndex(request):
#     return render(request, 'teacherIndex.html')


def teacher_list(request):
    return render(request, 'teacherList.html')


def teacher_details(request, slug):
    return render(request, 'teacherDetails.html')


# list and details api teacher

def is_teacher(id):
    user = User.objects.filter(id=id).first()
    return user.groups.filter(name='Teacher_Group').exists()


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and is_teacher(request.user.id))


class TeacherList(ListAPIView):
    permission_classes = [IsTeacher]

    def get(self, request):
        data = Teacher.objects.filter().prefetch_related('teacherEducation', 'teacherExperience').all()
        data = TeacherListSerializer(data, many=True).data
        return Response(data)


class TeacherDetails(ListAPIView):
    permission_classes = [IsTeacher]

    def get(self, request, slug):
        data = Teacher.objects.filter(slug=slug).first()
        data = TeacherDetailsSerializer(data).data
        return Response(data)