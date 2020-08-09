from rest_framework import viewsets
from .serializers import CourseSerializer,VideoSerializer,SubscribtionSerializer
from .models import Course,Video,Subscription

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer 

class SubscriptionViewset(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscribtionSerializer 