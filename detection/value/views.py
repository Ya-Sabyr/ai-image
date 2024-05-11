from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ValueForm
from .models import Value

def value_form_view(request):
    if request.method == 'POST':
        form = ValueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('value:results')
    else:
        form = ValueForm()
    return render(request, 'value/index.html', {'form': form})

def virus(request):
    return render(request, 'value/virus.html')

def bacteria(request):
    return render(request, 'value/bacter.html')

def covid(request):
    return render(request, 'value/covid.html')

def tuberc(request):
    return render(request, 'value/tuberc.html')

def instructions(request):
    return render(request, 'value/instructions.html')