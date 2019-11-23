from django.urls import path
from . import views

urlpatterns = [
    path('teens/', views.teens_list, name='teens'),
    path('teens/new/', views.teen_new, name='teen_new'),
]