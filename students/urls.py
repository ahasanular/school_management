from django.urls import path
from students import views

urlpatterns = [
    # path('', views.studentIndex),
    path('student_list/', views.student_list),
    path('details/<slug:slug>/', views.student_details),

    # list and detais view API
    path('student_list_api/', views.StudentList.as_view()),
    path('student_details_api/<slug:slug>/', views.StudentDetails.as_view()),
]