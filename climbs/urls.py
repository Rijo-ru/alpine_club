from django.urls import path
from . import views

urlpatterns = [
    path('', views.climb_list, name='climb_list'),
    path('add_mountain/', views.add_mountain, name='add_mountain'),
    path('add_climber/', views.add_climber, name='add_climber'),
    path('add_climb/', views.add_climb, name='add_climb'),
]
