from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
	""" Serializers a name Field for Testing our APIView. """
	name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
	""" A serializer for our user profile objects """

	class Meta:
		""" Tells the Serializer class what 
		fields we wanna take from our model """
		model = models.UserProfile
		fields = ('id','email','name','password')
		extra_kwargs = {'password':{'write_only':True}}


	def create(self, validated_data):
		""" Create and validate a new User"""
		user = models.UserProfile(
				email =validated_data['email'],
				name = validated_data['name']
			)

		user.set_password(validated_data['password'])
		user.save()

		return user