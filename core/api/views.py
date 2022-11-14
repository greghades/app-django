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

