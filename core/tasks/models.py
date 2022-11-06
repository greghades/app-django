from django.db import models

# Create your models here.
class Task_Model(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=250, blank=True,null=True)

    def __str__(self):
        return self.title
    