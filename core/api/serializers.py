from rest_framework.serializers import ModelSerializer
from tasks.models import Task_Model

class TaskSerializers(ModelSerializer):
    
    class Meta:
        model = Task_Model
        fields = '__all__'