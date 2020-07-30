from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=300)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.course_name

class Subscription(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    subsribed_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course} subscribed by {self.subscribed_by}"

class Video(models.Model):
    video_title = models.CharField(max_length=200)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now) 
    notes = models.TextField()
    #video_file = models.FileField()

    def __str__(self):
        return self.video_title