from django.urls import path
from . import views

urlpatterns = [
    # path('', views.teacherIndex),
    path('teacher_list/', views.teacher_list),
    path('details/<slug:slug>/', views.teacher_details),

    # list and details API
    path('teacher_list_api/', views.TeacherList.as_view()),
    path('teacher_details_api/<slug:slug>/', views.TeacherDetails.as_view()),
]