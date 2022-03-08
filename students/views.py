from django.shortcuts import render
from .models import Student


def studentIndex(request):
    return render(request, 'studentIndex.html')

def studentList(request):
    return render(request, 'studentList.html')

#from django.db.models import Q

def studentDetails(request, slug):
    return render(request, 'studentDetails.html')


#all api

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import StudentListSerializer, StudentDetailsSerializer
from django.contrib.auth.models import User




from rest_framework.permissions import BasePermission

def is_student(id):
    user = User.objects.filter(id=id).first()
    return user.groups.filter(name='Student_Group').exists()

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and is_student(request.user.id))


class StudentList(ListAPIView):
    permission_classes = [IsStudent]     #restrict access
    def get(self, request):
        data_val = Student.objects.filter().prefetch_related('studentClassInfo').all()
        data_val = StudentListSerializer(data_val, many=True).data
        return Response(data_val)

class StudentDetails(ListAPIView):
    permission_classes = [IsStudent]  # restrict access

    def get(self, request, slug):
        data = Student.objects.filter(slug=slug).first()
        data = StudentDetailsSerializer(data).data
        return Response(data)
