from django.urls import path
from . import views
from .views import signup_view, login_view, index, user_logout, profil

urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),
    path('SpeichernProfilbild/', profil, name='Profil'),
    path('save-residence/', views.save_residence, name='save_residence'),
    path('save-userpic/', views.save_userpic, name='save_userpic'),
]
