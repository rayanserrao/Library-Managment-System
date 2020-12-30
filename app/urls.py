from django.urls import path
from app.views import *

urlpatterns = [
    path('',home, name = 'home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('signup/',signup,name='signup')
]