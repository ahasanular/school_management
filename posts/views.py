import prefetch as Prefetch
from django.shortcuts import render
from .models import Posts, PostLikes
from students.models import Student
from teachers.models import Teacher
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_208_ALREADY_REPORTED
import json
from .serializers import PostsSerializer
from django.db.models import F, Count
from django.db.models.query import Prefetch
# end of import


# function based frontend views

def posts(request):
    return render(request, 'posts.html')


# api

class CreatePost(CreateAPIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            user = request.user
            is_text = True
            is_image = True
            if 'post_text' not in data or data['post_text'] == '':
                is_text = False

            if 'post_picture' not in data or data['post_picture'] == '' or not request.FILES['post_picture']:
                is_image = False

            if not is_text and not is_image:
                feedback = {'message': "Both Text and Image Can't be NULL !", 'status': HTTP_400_BAD_REQUEST}
                return Response(feedback)

            posts = Posts()
            posts.user = user
            posts.post_by = user.first_name + " " + user.last_name

            if is_text:
                posts.text = data['post_text']
            if is_image:
                posts.img = request.FILES['post_picture']

            if data['account_type'] == 'Student':
                person_obj = Student.objects.filter(email=request.user.email).first()
                posts.student = person_obj
            elif data['account_type'] == 'Teacher':
                person_obj = Teacher.objects.filter(email=request.user.email).first()
                posts.teacher = person_obj
            else:
                return Response({"message": "Account_Type_is_not_valid !"}, status=HTTP_400_BAD_REQUEST)

            if person_obj or person_obj != '':
                posts.save()

                feedback = {'message': "Post uploaded successfully !", 'status': HTTP_200_OK}
                return Response(feedback)
            else:
                feedback = {'message': "No User Found with this account Type !", 'status': HTTP_400_BAD_REQUEST}
                return Response(feedback)

        except Exception as ex:
            feedback = {'message': str(ex), 'status': HTTP_400_BAD_REQUEST}
            return Response(feedback)


class PostList(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            # data = Posts.objects.filter().annotate(image_student=F('student__img')).annotate(image_teacher=F(
            # 'teacher__img')).all() this is comment
            data = Posts.objects.filter().prefetch_related(Prefetch("post_like", PostLikes.objects.filter(user=user).all())).annotate(total_likes=Count("post_like")).all().order_by('-created_at')
            data = PostsSerializer(data, many=True).data
            return Response(data)
        except Exception as ex:
            feedback = {'message': str(ex), 'status': HTTP_400_BAD_REQUEST}
            return Response(feedback)


class LikesCount(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user

            if 'id' not in data or data['id'] == '':
                feedback = {'message': "Post Id No FOUND !", 'status': HTTP_400_BAD_REQUEST}
                return Response(feedback)

            # pre_likes = PostLikes.objects.filter(post=post).all()
            is_liked = PostLikes.objects.filter(user=user, post__id=data['id']).exists()

            if is_liked:
                feedback = {'message': "Already Liked !", 'status': HTTP_208_ALREADY_REPORTED}
                return Response(feedback)
            else:
                if not user:
                    feedback = {'message': "User No FOUND !", 'status': HTTP_400_BAD_REQUEST}
                    return Response(feedback)

                post = Posts.objects.filter(id=data['id']).first()

                likes = PostLikes()
                likes.user = user
                likes.post = post
                likes.save()

                sum_of_likes = PostLikes.objects.filter(post=post).all()

                feedback = {}
                feedback['message'] = "Post updated successfully !"
                feedback['status'] = HTTP_200_OK
                feedback['id'] = str(data['id'])
                feedback['likes'] = str(sum_of_likes.count())

                return Response(feedback)
        except Exception as ex:
            feedback = {'message': str(ex), 'status': HTTP_400_BAD_REQUEST}
            return Response(feedback)


class PostCreateApi(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # user = User.objects.get(id=request.user.id)
        post = Posts()
        post.user = request.user
        post.text = request.data['text']
        post.save()
        return Response("Success")