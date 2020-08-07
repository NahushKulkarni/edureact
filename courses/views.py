from django.shortcuts import render
from .models import Video,Course
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import TemplateView
# Create your views here.
@xframe_options_exempt
def VideoView(request):
    context={
        'videos':Video.objects.all()
    }
    return render(request,"courses/videos.html",context)

def CoursesView(request):
    context={
        'courses':Course.objects.all()
    }
    return render(request,"courses/courses.html",context)