from django import forms

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name","last_name")

class UserChangeForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username", "email" ,"first_name","last_name")