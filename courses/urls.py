from django.urls import path
from .api import CourseViewSet,VideoViewSet,SubscriptionViewset
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api/courses',CourseViewSet,'courses')
router.register('api/video',VideoViewSet,'video')
router.register('api/subscribe',SubscriptionViewset,'subscribe')
urlpatterns = router.urls