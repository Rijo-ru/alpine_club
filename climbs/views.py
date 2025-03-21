from django.shortcuts import render, get_object_or_404, redirect
from .models import Mountain, Climber, Climb

def climb_list(request):
    climbs = Climb.objects.all()
    return render(request, 'climbs/climb_list.html', {'climbs': climbs})

def climb_detail(request, pk):
    climb = get_object_or_404(Climb, pk=pk)
    return render(request, 'climbs/climb_detail.html', {'climb': climb})

def climb_create(request):
    if request.method == "POST":
        # Обработка данных формы
        pass
    else:
        # Отображение формы
        pass
    return render(request, 'climbs/climb_form.html')

def climb_update(request, pk):
    climb = get_object_or_404(Climb, pk=pk)
    if request.method == "POST":
        # Обработка данных формы
        pass
    else:
        # Отображение формы
        pass
    return render(request, 'climbs/climb_form.html', {'climb': climb})

def climb_delete(request, pk):
    climb = get_object_or_404(Climb, pk=pk)
    if request.method == "POST":
        climb.delete()
        return redirect('climb_list')
    return render(request, 'climbs/climb_confirm_delete.html', {'climb': climb})
