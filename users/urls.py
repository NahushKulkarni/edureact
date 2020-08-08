from .api import StudentViewSet,TeacherViewSet
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register("api/student",StudentViewSet,"student")
router.register("api/teacher",TeacherViewSet,"teacher")
urlpatterns = router.urls 