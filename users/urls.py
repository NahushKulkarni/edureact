from .api import StudentViewSet,TeacherViewSet
from django.urls import path
from .views import register  
from rest_framework import routers
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register("api/student",StudentViewSet,"student")
router.register("api/teacher",TeacherViewSet,"teacher")
urlpatterns = router.urls + [path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
                             path('register/', register ,name = 'register')]
