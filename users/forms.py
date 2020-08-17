from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm

#test comment
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    Email = forms.EmailField(label='Email', max_length=100)
    linkedin = forms.CharField(label='Linkedin', max_length=100)
    github = forms.CharField(label='Github', max_length=100)

    class Meta:
        model = Student
        fields = ['username', 'first_name','last_name','Email','linkedin','github','password1','password2']

class userupdateform(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Student
        fields = ['username','email']

class profileupdateform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['image']