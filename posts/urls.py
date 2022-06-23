from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts),

    # create post api
    path('create_post_api/', views.CreatePost.as_view()),
    path('post_list_api/', views.PostList.as_view()),
    path('likes_api/', views.LikesCount.as_view()),
    path('test/', views.PostCreateApi.as_view()),
]