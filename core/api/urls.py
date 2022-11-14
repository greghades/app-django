from django.urls import path
from .views import getTask,postTask
urlpatterns = [
    path('api/getTask/',getTask,name='getTask'),
    path('api/postTask/',postTask,name='postTask'),
]
