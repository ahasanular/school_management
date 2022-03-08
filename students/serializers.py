from rest_framework import serializers
from .models import Student,StudentClassInfo


class StudentClassInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClassInfo
        fields = ['std_class', 'roll', 'section', 'admission_date']

class StudentListSerializer(serializers.ModelSerializer):
    studentClassInfo = StudentClassInfoSerializer(many=True)
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'gender', 'email', 'phone', 'address', 'img', 'slug', 'studentClassInfo']

class StudentDetailsSerializer(serializers.ModelSerializer):
    studentClassInfo = StudentClassInfoSerializer(many=True)
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'fathers_name', 'mothers_name', 'gender', 'religion', 'birth_date', 'email', 'phone', 'address', 'blood_group', 'img', 'studentClassInfo']