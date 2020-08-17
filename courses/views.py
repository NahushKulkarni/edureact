from django.shortcuts import render
from .models import Video,Course
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import TemplateView
from django.http import request
from users.models import Student,Teacher
# Create your views here.
@xframe_options_exempt
def VideoView(request):
    context={
        'course':Video.objects.get(course=request.get('C',default=None))
        'video':Video.objects.get(video_title=request.get('V',default=None))
        # 'user':Student.objects.get(username=request.get('U',default=None))
        'user':Student.objects.get(username=request.user.username))
    }
    return render(request,"courses/videos.html",context)

def CoursesView(request):
    context={
        'courses':Course.objects.all()
        # 'user':Student.objects.get(username=request.get('U',default=None))
        'user':Student.objects.get(username=request.user.username))
    }
    return render(request,"courses/courses.html",context)