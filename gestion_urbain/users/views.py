from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Ce nom d'utilisateur est déjà pris.")
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.success(request, "Compte créé avec succès ! Connectez-vous.")
                return redirect("login")
        else:
            messages.error(request, "Les mots de passe ne correspondent pas.")
    
    return render(request, "users/register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, "users/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")
