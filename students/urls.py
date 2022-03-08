from django.urls import path
from students import views

urlpatterns = [
    path('', views.studentIndex),
    path('student_list/', views.studentList),
    path('details/<slug:slug>/', views.studentDetails),

    #list and detais view api
    path('student_list_api/', views.StudentList.as_view()),
    path('student_details_api/<slug:slug>/', views.StudentDetails.as_view()),
]