from rest_framework import serializers
from django.contrib.auth.models import User
from classes.models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ["subject", "year", "teacher"]

class ClassroomDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'

class CreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ["subject", "year"]

