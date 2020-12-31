from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control md-6'}))
    password2 = forms.CharField(label=' Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control md-6'}))

    class Meta:
        model = User
        fields =['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control md-6'}),
        'first_name':forms.TextInput(attrs={'class':'form-control md-6'}),
        'last_name':forms.TextInput(attrs={'class':'form-control md-6'}),
        'email':forms.EmailInput(attrs={'class':'form-control md-6'})


        
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label='Password',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control '}))

class Passwordchangeform1(PasswordChangeForm):
    old_password = forms.CharField(label= 'Old Password',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control md-4' 'required'}) )
    new_password1 = forms.CharField(label= 'New Password',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control md-4 ' 'required'}) )
    new_password2 = forms.CharField(label= 'Confirm Password',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control md-4' 'required'}) )

class PasswordChangeform2(SetPasswordForm):
    new_password1 = forms.CharField(label= 'New Password',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control md-4 ' 'required'}) )
    new_password2 = forms.CharField(label= 'Confirm Password',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control md-4' 'required'}) )