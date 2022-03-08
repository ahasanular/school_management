from rest_framework import serializers
from .models import Footer

class FooterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'