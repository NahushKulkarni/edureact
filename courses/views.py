from django.shortcuts import render,get_object_or_404,redirect
from .models import Video,Course
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import TemplateView, ListView
from django.http import request
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Student,Teacher
from django.contrib.auth import logout
from users import views as userviews
# Create your views here.
@xframe_options_exempt
def VideoView(request):
    if not Student.objects.filter(username=request.user).exists():
        return redirect(userviews.register)
    
    query = request.GET
    C = int(query['C'])
    V = int(query['V'])
    if C != 0:
        cou = Video.objects.filter(course=C)
    else:
        return redirect(CoursesView)
    
    if V != 0:
        vid = cou.filter(id=V)
    else:
        vid = cou.filter(id=1)

    context={
        'courses': cou,
        'video':vid
    }
    return render(request,"courses/videos.html",context)

def CoursesView(request):
    context={
        'courses':Course.objects.all(),
    }
    return render(request,"courses/courses.html",context)

def logout_request(request):
    logout(request)
    return redirect("home/")

class Home(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/home.html'
    #def get_queryset(self):
    #    user = get_object_or_404(Teacher ,user=self.kwargs.get('user'))