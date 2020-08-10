from .api import StudentViewSet,TeacherViewSet
from django.urls import path
from .views import register  
from rest_framework import routers

router = routers.DefaultRouter()
router.register("api/student",StudentViewSet,"student")
router.register("api/teacher",TeacherViewSet,"teacher")
urlpatterns = router.urls + [path('register/', register ,name = 'register')]