from LostObjectsAPI.models import LostObject, Place, Student
from LostObjectsAPI.serializers import LostObjectSerializer, PlaceSerializer, StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def lost_object(request, format=None):
    if request.method == 'GET':
        los = LostObject.objects.all()[:15]
        if len(los) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LostObjectSerializer(los, many=True)
        return Response({'LostObjects': serializer.data})
    if request.method == 'POST':
        serializer = LostObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def lostobject_details(request, id, format=None):
    try:
        lo = LostObject.objects.get(pk=id)
    except LostObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LostObjectSerializer(lo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LostObjectSerializer(lo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        lo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def valid_place(request, format=None):
    if request.method == 'GET':
        place = Place.objects.all()
        if len(place) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PlaceSerializer(place, many=True)
        return Response({'Places': serializer.data})
    if request.method == 'POST':
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def lostobject_by_place(request, id, format=None):
    try:
        lo = LostObject.objects.filter(place=id)
    except LostObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if len(lo) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LostObjectSerializer(lo, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def lostobject_by_important(request, format=None):
    try:
        lo = LostObject.objects.filter(important=True)
    except LostObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if len(lo) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LostObjectSerializer(lo, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def lostobject_by_not_important(request, format=None):
    try:
        lo = LostObject.objects.filter(important=False)
    except LostObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if len(lo) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LostObjectSerializer(lo, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def lostobject_by_name(request, obj_name, format=None):
    try:
        lo = LostObject.objects.filter(
            object_name__startswith=obj_name.capitalize())
    except LostObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if len(lo) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LostObjectSerializer(lo, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def student(request, format=None):
    if request.method == 'GET':
        ss = Student.objects.all()[:15]
        if len(ss) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(ss, many=True)
        return Response({'Students': serializer.data})
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def student_details(request, register, format=None):
    try:
        s = Student.objects.get(register=register)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(s)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(s, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        s.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
