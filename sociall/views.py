from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from . import accountmanagement
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Index
def index(request):
    userpic = accountmanagement.getuserpic(request) # HIER PROBLEM
    context = {"userpic": userpic}
    return render(request, 'index.html', context)

# Profileinstellung
def profil(request):
    return render(request, "SpeichernProfilbild2.html")

def Datenschutz(request):
    return render(request, "Datenschutzerklärung.html")

def Impressum(request):
    return render(request, "Impressum.html")

# Registrieren
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(User.objects.make_random_password()) #geht nicht ohne passwort. Aber so wenigstens mit random-passwort, was nicht wieder benutzt werden muss.
            user.save()
            login(request, user)
            accountmanagement.createprofile(request)
            #accountmanagement.setresidence(request) #Steht hier nur zum PROBIEREN!
            #accountmanagement.setuserpic(request) #HIER PROBLEM
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Anmelden
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.filter(username=username).first()
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('username', 'Ungültiger Benutzername')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Abmelden
def user_logout(request):
    logout(request)
    return redirect('login')

# Wohnort speichern beim Klick auf "Wohnort speichern"
@csrf_exempt
def save_residence(request):
    if request.method == 'POST':
        accountmanagement.setresidence(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

# Profilbild speichern beim Klick auf "Profilbild ändern"
@csrf_exempt
def save_userpic(request):
    if request.method == 'POST':
        accountmanagement.setuserpic(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)
