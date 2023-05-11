from django.urls import path
from menu.views import (MenuHomeView,
)
from .views import HomeView, CustomLoginView, FoodView, AboutView, OrderView, PaymentView
from django.contrib.auth.views import LogoutView
from .views import profile
from hr_management.views import signup_view, profile_update

urlpatterns = [
    #front-end
    path('', HomeView.as_view(), name='home'),
    path('menus/', MenuHomeView.as_view(), name='menu_home'),
    path('payment', PaymentView.as_view(), name='payment'),
    path('about/', AboutView.as_view(), name='about'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('foods/', FoodView.as_view(), name='foods'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', profile_update, name='profile-update'),
    path('signup/', signup_view, name="signup")
]