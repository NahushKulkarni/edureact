from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    #tutor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
        

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    
    

    def __str__(self):
        return self.user.username