from django.shortcuts import render,redirect
from app.forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Signup succesfully')
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})


def loginuser(request):
    if request.method == 'POST':
        form = LoginForm(request = request, data = request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)


                messages.success(request,'Logged in successfully')
                return redirect('/')
    
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})
    
