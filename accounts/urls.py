from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.users_list, name='users'),
    path('accounts/new/', views.user_new, name='user_new'),
    path('accounts/<int:pk>/deactivate/', views.user_change_is_active, name='user_change_is_active'),
    path('password/', views.change_password, name='change_password'),
    path('accounts/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('accounts/<int:pk>/reset-password/', views.user_reset_password, name='user_reset_password'),
    
]