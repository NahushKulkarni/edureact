from django.shortcuts import render,get_object_or_404
from .models import Video,Course
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import TemplateView, ListView
from django.http import request
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Student,Teacher
# Create your views here.
@xframe_options_exempt
def VideoView(request):
    try:
        context={
            'course':Video.objects.get(course_name=request.get('C',default=None)),
            'video':Video.objects.get(video_title=request.get('V',default=None)),
            # 'user':Student.objects.get(username=request.get('U',default=None))
            #'user':Student.objects.get(username=request.user)
        }
    except:
        context={
            'course':Video.objects.all(),
            'video':Video.objects.all(),
            # 'user':Student.objects.get(username=request.get('U',default=None))
            #'user':Student.objects.get(username=request.user)
        }
    return render(request,"courses/videos.html",context)

def CoursesView(request):
    context={
        'courses':Course.objects.all(),
        # 'user':Student.objects.get(username=request.get('U',default=None))
        #'user':Student.objects.get(username=request.user)
    }
    return render(request,"courses/courses.html",context)
class Home(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/home.html'
    #def get_queryset(self):
    #    user = get_object_or_404(Teacher ,user=self.kwargs.get('user'))