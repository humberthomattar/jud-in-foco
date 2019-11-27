from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.users_list, name='users'),
    path('accounts/new/', views.user_new, name='user_new'),
    path('accounts/<int:pk>/deactivate/', views.user_change_is_active, name='user_change_is_active'),
    path('password/', views.change_password, name='change_password'),
]