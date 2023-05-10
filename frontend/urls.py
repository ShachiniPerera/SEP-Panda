from django.urls import path
from menu.views import (MenuHomeView,
)
from .views import HomeView, CustomLoginView
from django.contrib.auth.views import LogoutView
from .views import profile
from hr_management.views import signup_view

urlpatterns = [
    #front-end
     path('', HomeView.as_view(), name='home'),
    path('menus/', MenuHomeView.as_view(), name='menu_home'),
     path('login', CustomLoginView.as_view(), name='login'),
     path('logout', LogoutView.as_view(), name='logout'),
     path('profile/', profile, name='profile'),
     path('signup/', signup_view, name="signup")
]