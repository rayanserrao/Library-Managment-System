from django.shortcuts import render,redirect
from app.forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages 

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
            return redirect('/')
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})
    
