from django.shortcuts import render,get_object_or_404
from .models import Video,Course
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Student,Teacher
# Create your views here.
@xframe_options_exempt
def VideoView(request):
    context={
        'videos':Video.objects.all()
    }
    return render(request,"courses/videos.html",context)

def CoursesView(request):
    context={
        'courses':Course.objects.all(),
    }
    return render(request,"courses/courses.html",context)
class Home(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/home.html'
    #def get_queryset(self):
    #    user = get_object_or_404(Teacher ,user=self.kwargs.get('user'))