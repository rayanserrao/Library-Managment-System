from django.urls import path
from app.views import *

urlpatterns = [
    path('',home, name = 'home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('signup/',signup,name='signup'),
    path('login/',loginuser,name='loginuser'),
    path('logout/',logoutuser,name='logoutuser')
]