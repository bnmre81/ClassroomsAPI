from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from classes.models import Classroom
from .serializers import ClassroomSerializer, ClassroomDetailsSerializer, CreateSerializer
# Create your views here.

class APIListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer


class APIDetailsView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'    

class ClassroomCreate(CreateAPIView):
	serializer_class = CreateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)

class ClassroomUpdate(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = CreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'

class CancelClassroom(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'



	