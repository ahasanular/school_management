from django.urls import path
from . import views

urlpatterns = [
    path('', views.signUp),
    path('verification/<str:account_type>/<str:email>/<str:otp>/', views.verification),

    #api
    path('sign_up_api/', views.SignUp.as_view()),
    path('otp_check_api/', views.OtpCheck.as_view()),
    path('send_verification_api/', views.SendVerificationLink.as_view()),
]