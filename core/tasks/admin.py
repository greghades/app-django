from django.contrib import admin
from .models import Task_Model,Priority


# Register your models here.
admin.site.register(Task_Model)
admin.site.register(Priority)