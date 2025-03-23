from django.contrib import admin
from django.urls import path, include
from climbs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('climbs/', include('climbs.urls')),
    path('', views.home, name='home'),
]
