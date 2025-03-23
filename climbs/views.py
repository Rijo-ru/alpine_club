from django.shortcuts import render, redirect
from .forms import MountainForm, ClimberForm, ClimbForm
from .models import Climb

def home(request):
    climbs = Climb.objects.all()
    return render(request, 'climbs/home.html', {'climbs': climbs})

def climb_list(request):
    climbs = Climb.objects.all()
    return render(request, 'climbs/climb_list.html', {'climbs': climbs})

def add_mountain(request):
    if request.method == 'POST':
        form = MountainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('climb_list')
    else:
        form = MountainForm()
    return render(request, 'climbs/add_mountain.html', {'form': form})

def add_climber(request):
    if request.method == 'POST':
        form = ClimberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('climb_list')
    else:
        form = ClimberForm()
    return render(request, 'climbs/add_climber.html', {'form': form})

def add_climb(request):
    if request.method == 'POST':
        form = ClimbForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('climb_list')
    else:
        form = ClimbForm()
    return render(request, 'climbs/add_climb.html', {'form': form})
