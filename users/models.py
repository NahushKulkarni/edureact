from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractUser
#from courses.models import Course
# Create your models here.

class Student(AbstractUser):
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    teacher_status = models.BooleanField('teacher_status',default=False)
    #tutor = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height>100 or img.width>100:
            output_size=(100,100)
            img.thumbnail(output_size)
            img.save(self.image.path)
        

class Teacher(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)
    course_uploaded = models.CharField(max_length=100)
    

    def __str__(self):
        return self.user.username