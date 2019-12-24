from django.shortcuts import render
from rest_framework import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .serializers import UserSerializer
from .models import Student
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

#Create your views here.
class studentsView(viewsets.Viewset):

	def list(self, request):
		queryset = Student.object.all()
		serializer = StudentSerializer(queryset, many=True)
		return Response(serializer.data)