from rest_framework import serializers
from LostObjectsAPI.models import LostObject, Place, Student


class LostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostObject
        fields = ['id', 'object_name', 'place', 'img', 'important',]


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'faculty',]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['register', 'first_name', 'last_name']
