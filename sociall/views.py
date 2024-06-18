from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from . import accountmanagement

# Gehört in das Dropdownmenü oben rechts!
def profil(request):
    return render(request, 'SpeichernProfilbild2.html')
          
# Home page          
def index(request):
    return render(request, 'index.html')

# signup page
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(User.objects.make_random_password()) #geht nicht ohne passwort. Aber so wenigstens mit random-passwort, was nicht wieder benutzt werden muss.
            user.save()
            login(request, user)
            accountmanagement.createprofile(request)
            accountmanagement.setresidence(request) #gehört dann an die Stelle, an der der Wohnort übergeben wird!
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
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

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
