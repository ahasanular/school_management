from rest_framework import serializers
from .models import Teacher, TeacherEducation, TeacherExperience

class TeacherEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherEducation
        fields = ['teacher_edu', 'speciality', 'passing_year']

class TeacherExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherExperience
        fields = ['exp_name', 'exp_start_date', 'exp_end_date', 'exp_designation', 'speciality']

class TeacherListSerializer(serializers.ModelSerializer):
    teacherEducation = TeacherEducationSerializer(many=True)
    teacherExperience = TeacherExperienceSerializer(many=True)
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'gender', 'email', 'phone', 'address', 'img', 'salary', 'slug', 'teacherEducation', 'teacherExperience']

class TeacherDetailsSerializer(serializers.ModelSerializer):
    teacherEducation = TeacherEducationSerializer(many=True)
    teacherExperience = TeacherExperienceSerializer(many=True)
    class Meta:
        model = Teacher
        fields = ['full_name', 'fathers_name', 'gender', 'religion', 'birth_date', 'email', 'phone', 'address', 'blood_group', 'nationality', 'img', 'salary', 'teacherEducation', 'teacherExperience']