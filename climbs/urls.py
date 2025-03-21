from django.urls import path
from . import views

urlpatterns = [
    path('', views.climb_list, name='climb_list'),
    path('<int:pk>/', views.climb_detail, name='climb_detail'),
    path('new/', views.climb_create, name='climb_create'),
    path('<int:pk>/edit/', views.climb_update, name='climb_update'),
    path('<int:pk>/delete/', views.climb_delete, name='climb_delete'),
]
