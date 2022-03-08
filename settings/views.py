from django.shortcuts import render
from .models import Footer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import FooterInfoSerializer

class FooterInfo(ListAPIView):
    permission_classes = []
    def get(self, request):
        data = Footer.objects.filter().first()
        data= FooterInfoSerializer(data).data
        return Response(data)


class IPAddress(ListAPIView):
    permission_classes = []
    def get(self, request):
        print(request.META)
        return Response(request.META.get('REMOTE_ADDR'))