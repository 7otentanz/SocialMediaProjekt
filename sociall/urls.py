from django.urls import path
from . import views
from .views import signup_view, login_view, index, user_logout, profil, datenschutz, impressum

urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),
    path('SpeichernProfilbild/', profil, name='Profil'),
    path('save-residence/', views.save_residence, name='save_residence'),
    path('save-userpic/', views.save_userpic, name='save_userpic'),
    path('Datenschutzerklärung/', datenschutz, name='datenschutz'),
    path('Impressum/', impressum, name='impressum'),
    path('add_post/', views.add_post, name='add_post'),
    path('get_all_posts/', views.get_all_posts, name='get_all_posts'),
    path('like_post/<int:post_id>/', views.handle_like, name='like_post'),
    path('dislike_post/<int:post_id>/', views.handle_dislike, name='dislike_post'),
    path('flag_post/<int:post_id>/', views.handle_flag, name='flag_post'),
]
