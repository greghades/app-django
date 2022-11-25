from django.urls import path
from .views import getTask,postTask,putTask,deleteTask
urlpatterns = [
    path('api/getTask/',getTask,name='getTask'),
    path('api/postTask/',postTask,name='postTask'),
    path('api/putTask/<int:pk>',putTask,name='putTask'),
    path('api/deleteTask/<int:pk>',deleteTask,name='deleteTask')
]
