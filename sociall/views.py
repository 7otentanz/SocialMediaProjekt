from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm


# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Set a default password as Django requires it, but user won't use it for login
            user.set_password(User.objects.make_random_password())
            user.save()
            # Automatically log the user in after signup
            login(request, user)
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