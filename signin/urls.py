from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in),
    path('log_out/', views.log_out),

    path('my_account/', views.my_dashboard),
    path('my_account_api/<str:name>/', views.MyDashboard.as_view()),

]