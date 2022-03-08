from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignIn),
    path('log_out/', views.log_out),

    path('my_account/', views.myDashboard),
    path('my_account_api/<str:name>/', views.MyDashboard.as_view()),

]