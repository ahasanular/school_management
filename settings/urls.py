from django.urls import path
from . import views

urlpatterns = [
    path('', views.IPAddress.as_view()),
]