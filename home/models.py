from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    content=models.TextField(max_length=20)   
    draft=models.BooleanField(default=False)

    def __str__(self):
        return self.title