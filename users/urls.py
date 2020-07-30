from .api import StudentViewSet,TeacherViewSet,UserViewSet
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register("api/student",StudentViewSet,"student")
router.register("api/teacher",TeacherViewSet,"teacher")
router.register("api/user",UserViewSet,"user")
urlpatterns = router.urls