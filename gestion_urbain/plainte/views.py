from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def home(request):
    return render(request, 'plainte/home.html')

def accueil(request):
    plaintes = Plainte.objects.filter(user=request.user)  # Récupère les signalements de l'utilisateur connecté
    return render(request, 'plainte/accueil.html', {'plaintes': plaintes})


def ajout_plaintes(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user  
            report.save()
            return redirect('home')
    else:
        form = ReportForm()

    return render(request, 'plainte/ajout_plaintes.html', {'form': form})


def modifier(request, report_id):
    report = get_object_or_404(Plainte, id=report_id, user=request.user)

    if request.method == "POST":
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReportForm(instance=report)

    return render(request, 'plainte/modifier.html', {'form': form, 'report': report})


def supp(request, report_id):
    report = get_object_or_404(Plainte, id=report_id, user=request.user)

    if request.method == "POST":
        report.delete()
        return redirect('home')

    return render(request, 'plainte/supp.html', {'report': report})


def detail_plainte(request, report_id):
    report = get_object_or_404(Plainte, id=report_id)
    
    return render(request, 'plainte/detail.html', {'report': report})
