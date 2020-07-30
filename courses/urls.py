from django.urls import path
from .api import CourseViewSet,VideoViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api/courses',CourseViewSet,'courses')
router.register('api/video',VideoViewSet,'video')

urlpatterns = router.urls