#from .forms import TeenForm
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def teens_list(request):
    return render(request, 'teens/teens.html')

def teen_new(request):
    return render(request, 'teens/teen_new.html')
