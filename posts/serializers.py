from rest_framework import serializers
from .models import Posts, PostLikes
from django.contrib.auth.models import User
from students.models import Student
from teachers.models import Teacher



class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'slug', 'img']

class TeacherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'email', 'slug', 'img']

class LikeCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikes
        fields = ["user"]

class PostsSerializer(serializers.ModelSerializer):
    # postUser = PostsUserSerializer(many=True)
    total_likes = serializers.CharField()
    post_like = LikeCountSerializer(many=True)
    student = StudentDataSerializer(many=False)
    teacher = TeacherDataSerializer(many=False)
    class Meta:
        model = Posts
        fields = ['id', 'post_by', 'text', 'img', 'created_at', 'user', 'student', 'teacher', 'total_likes', 'post_like']