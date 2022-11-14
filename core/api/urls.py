from django.urls import path
from .views import getTask
urlpatterns = [
    path('api/getTask/',getTask,name='getTask')
]
