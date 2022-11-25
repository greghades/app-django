from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks.models import Task_Model
from .serializers import TaskSerializers

# Create your views here.


@api_view(['GET'])
def getTask(request):
    tasks = Task_Model.objects.all()
    serializers = TaskSerializers(tasks, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def postTask(request):
    
    serializers = TaskSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)

@api_view(['PUT'])
def putTask(request,pk):
    user = Task_Model.objects.filter(id = pk).first()
    serializers = TaskSerializers(user,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)

@api_view(['DELETE'])
def deleteTask(request,pk):
    user = Task_Model.objects.filter(id = pk).first()
    user.delete()
    return Response('Usuario eliminado con exito')
