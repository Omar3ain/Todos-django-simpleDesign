from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    name = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    
class TodoItems(models.Model):
    name = models.CharField(max_length=150 , null=True , blank=True)
    createAt = models.DateTimeField(auto_now_add=True , null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    isCompleted = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    def getDescriptions(self):
        return self.description[:30]
    
