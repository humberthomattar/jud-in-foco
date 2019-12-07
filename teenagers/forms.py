from django import forms
from .models import Teenager

class TeenagerForm(forms.ModelForm):

    class Meta:
        model = Teenager
        fields = (
                'name',       
                'name_mother',
                'name_father',
                'date_birth',
                'type_sex',
                'address',
                'notes'
                )

class TeenagerChangeForm(forms.ModelForm):
    
    class Meta:
        model = Teenager
        fields = [
                'name',       
                'name_mother',
                'name_father',
                'date_birth',
                'type_sex',
                'address',
                'notes'
        ]