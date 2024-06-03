from django.urls import path
from . import views
from .views import signup_view, login_view, index, user_logout

urlpatterns = [
    path('', index, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),
]