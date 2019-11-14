from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.users_list, name='users'),
    path('accounts/new/', views.user_new, name='user_new'),
]