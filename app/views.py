from django.shortcuts import render,redirect
from app.forms import SignupForm,LoginForm,Passwordchangeform1,PasswordChangeform2
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm


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

def logoutuser(request):
    if request.user.is_authenticated:


        logout(request)
        messages.info(request,'Logged Out successfully')
        return redirect('/login/')
    else:

        return redirect('/login/')

def userpasschange(request):
    if request.user.is_authenticated:
            
        if request.method == 'POST':
            form = Passwordchangeform1(user= request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"password changed successfully")
                update_session_auth_hash(request,form.user)
                return redirect('/')

        else:
            form = Passwordchangeform1(user = request.user)
        return render(request,'passchange1.html',{'form':form})
    else:
        return redirect('/login/')

def userchnagepass(request):
    
            
    if request.method == 'POST':
        form = PasswordChangeform2(user= request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"password changed successfully")
            update_session_auth_hash(request,form.user)
            return redirect('/login/')

    else:
        form =PasswordChangeform2(user = request.user)
    return render(request,'passchange2.html',{'form':form})
   


    
