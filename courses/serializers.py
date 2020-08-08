from rest_framework import serializers
from .models import Course,Video,Subscription

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__' 
class SubscribtionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__' 