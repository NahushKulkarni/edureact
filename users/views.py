#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login,authenticate
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    
""" def login_view(request):
    form = UserRegisterForm()
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        messages.success(request,f"Successfully logged in as {username}")
        return redirect('home-view')
    else:
        messages.error(request,f"Incorrect password or username")
    return render(request,'users/login.html',{'form':form})
 """    
