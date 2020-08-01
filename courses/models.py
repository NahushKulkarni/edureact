from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from users.models import Teacher,Student
from PIL import Image
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=300)
    instructor = models.ForeignKey('users.Teacher', on_delete=models.CASCADE,default=0)
    created_at = models.DateTimeField(default=timezone.now)
    course_image = models.ImageField(default="default.jpg",upload_to="course_pics")

    def __str__(self):
        return self.course_name

class Subscription(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    subsribed_by = models.ForeignKey('users.Student',on_delete=models.CASCADE,default=0)

    def __str__(self):
        return f"{self.course} subscribed by {self.subscribed_by}"

class Video(models.Model):
    video_title = models.CharField(max_length=200)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,default=0)
    created_at = models.DateField(default=timezone.now) 
    notes = models.TextField()
    video_file = models.FileField(default='default.jpg',upload_to='courses_videos',verbose_name="course_video")

    def __str__(self):
        return self.video_title