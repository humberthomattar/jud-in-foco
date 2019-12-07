from django.urls import path
from . import views

urlpatterns = [
    path('teenagers/', views.teenagers_list, name='teenagers'),
    path('teenagers/new/', views.teenager_new, name='teenager_new'),
    path('teenagers/<int:pk>/change_status/', views.teenager_change_status, name='teenager_change_status'),
    path('teenagers/<int:pk>/edit/', views.teenager_edit, name='teenager_edit'),
]