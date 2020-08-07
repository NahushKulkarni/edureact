from django.urls import path
from .api import CourseViewSet,VideoViewSet,SubscriptionViewset
from rest_framework import routers
from .models import Course,Video
from .views import VideoView
router = routers.DefaultRouter()
router.register('api/courses',CourseViewSet,'courses')
router.register('api/video',VideoViewSet,'video')
router.register('api/subscribe',SubscriptionViewset,'subscribe')
<<<<<<< HEAD
urlpatterns = router.urls + [path('videos',VideoView,name="video-view")]
=======
urlpatterns = router.urls + [path('videos',VideoView,name="video-view")]
>>>>>>> 883afbc8463749d40e320e4dc60f36183d93f1b3
