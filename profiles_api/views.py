from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication




from . import serializers
from . import models

from . import permissions



# Create your api view

class HelloApiView(APIView):
	""" Test API View """

	serializer_class = serializers.HelloSerializer

	def get(self, response, format=None):
		""" Returns a list of APIView features """

		an_apiview = [
			'Uses HTTP Method as function (get, post, putch, put, delete)'
			'It is similar to a traditional Django view',
			'Give you the most control over your logic',
			'It is mapped manually to URLS',
		]

		return Response({'message':'Hello!','an_apiview':an_apiview})

	def post(self, request):
		""" create a Hello Message with our name"""
		serializer = serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message':message})
		else:
			return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
	def put(self, request, pk=None):
		""" Handles updating an object """
		return Response({'method':'put'})

	def patch(self, request,pk=None):
		""" Putch request only updates fields provided in the request"""
		return Response({'method': 'patch'})

	def delete(self, request,pk=None):
		""" Deletes an object """

		return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
	""" Test API ViewSet"""



	serializer_class = serializers.HelloSerializer

	def list(self, request):
		""" Return a Hello message """
		a_viewset = [
			'Uses actions (list, create, retrieve, update, partial_update)',
			'Automatically maps to URLS using Routers',
			'Provides more functionality with less code',
		]

		return Response({'message':'Hello!','a_viewset':a_viewset})

	def create(self,request):
		""" Create a new hello message"""

		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message':message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def retrieve(self,request,pk=None):
		"""handles getting an object by ID"""
		return Response({'http_method':'GET'})

	def update(self,request, pk=None):
		""" Handles updating an object"""

		return Response({'http_method': 'PUT'})

	def partial_update(self,request,pk=None):
		return Response({'http_method':'PATCH'})

	def destroy(self,request,pk=None):
		""" Handles remooving an object"""
		return Response({'http_method':"DELETE_"})

class UserProfileViewSet(viewsets.ModelViewSet):
	""" Handles creating and updating profiles."""

	serializer_class = serializers.UserProfileSerializer

	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)