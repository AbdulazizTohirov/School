from rest_framework import serializers
from main.models import *

from django.contrib.auth.models import User

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFeedback
        fields = '__all__'
      
class  ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'
      
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']