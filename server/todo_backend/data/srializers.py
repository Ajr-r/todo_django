from rest_framework import serializers
from .models import Task_r
class Task_rSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task_r
        fields='__all__'