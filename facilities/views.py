from django.shortcuts import render
from .models import Facility

def facilityList(request):
    return render(request, 'facilityList.html')

def facilityDetails(request, id):
    return render(request, 'facilityDetails.html')


from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import FacilityListSerializer

from rest_framework.permissions import BasePermission
from students.views import IsStudent
from teachers.views import IsTeacher

class IsValidViewer(BasePermission):
    def checkViewer(self, IsStudent, IsTeacher):
        if(IsStudent):
            return True
        elif(IsTeacher):
            return True
        else:
            return False
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and self.checkViewer(IsStudent,IsTeacher))

class FacilityList(ListAPIView):
    permission_classes = [IsValidViewer]
    def get(self, request):
        data = Facility.objects.filter().all()
        data = FacilityListSerializer(data, many=True).data
        return Response(data)

class FacilityDetails(ListAPIView):
    permission_classes = [IsValidViewer]
    def get(self, request, id):
        data = Facility.objects.filter(id=id).first()
        data = FacilityListSerializer(data).data
        return Response(data)