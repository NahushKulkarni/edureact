from django.urls import path
from .api import CourseViewSet,VideoViewSet,SubscriptionViewset
from rest_framework import routers
from .models import Course,Video
from .views import VideoView, CoursesView
router = routers.DefaultRouter()
router.register('api/courses',CourseViewSet,'courses')
router.register('api/video',VideoViewSet,'video')
router.register('api/subscribe',SubscriptionViewset,'subscribe')
urlpatterns = router.urls + [path('videos/',VideoView,name="video-view")]
urlpatterns += [path('courses/',CoursesView,name="Courses-view")]