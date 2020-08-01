from rest_framework import viewsets
from .serializers import CourseSerializer,VideoSerializer
from .models import Course,Video

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer 