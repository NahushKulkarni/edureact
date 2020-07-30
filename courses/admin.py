from django.contrib import admin
from .models import Course,Subscription,Video

# Register your models here.
admin.site.register(Course)
admin.site.register(Subscription)
admin.site.register(Video)