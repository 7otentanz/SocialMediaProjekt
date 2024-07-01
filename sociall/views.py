from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from . import accountmanagement
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils import timezone

# Index
def index(request):
    userpic = accountmanagement.getuserpic(request)
    context = {"userpic": userpic}
    return render(request, 'index.html', context)

# Profileinstellung
def profil(request):
    return render(request, "SpeichernProfilbild2.html")

# Datenschutzerklärung
def datenschutz(request):
    return render(request, "Datenschutzerklärung.html")

# Impressum
def impressum(request):
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

@login_required
def add_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content')
        if content:
            post = Post.objects.create(user=request.user, content=content, created_at=timezone.now())
            return JsonResponse({'message': 'Post added successfully'})
        return JsonResponse({'message': 'Content cannot be empty'}, status=400)
    return JsonResponse({'message': 'Invalid request'}, status=400)

@login_required
def get_all_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    post_list = [{
        'user_id': post.user.id,
        'post_id': post.id,
        'datetime': post.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        'content': post.content,
        'likes': post.likes.count(),
        'dislikes': post.dislikes.count(),
        'flags': post.flags.count()
    } for post in posts]
    return JsonResponse(post_list, safe=False)

@login_required
def handle_like(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return JsonResponse({'likes': post.likes.count()})

@login_required
def handle_dislike(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
    return JsonResponse({'dislikes': post.dislikes.count()})

@login_required
def handle_flag(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user in post.flags.all():
        post.flags.remove(request.user)
    else:
        post.flags.add(request.user)
    if post.flags.count() > 5:
        post.delete()
        return JsonResponse({'message': 'Post removed due to flags'})
    return JsonResponse({'flags': post.flags.count()})