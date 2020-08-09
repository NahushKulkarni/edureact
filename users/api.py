from .serializers import StudentSerializer,TeacherSerializer
from .models import Student,Teacher
from django.contrib.auth.models import User
from rest_framework import viewsets
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer 