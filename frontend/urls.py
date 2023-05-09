from django.urls import path
from menu.views import (MenuHomeView,
)
from .views import HomeView
from django.views.generic import TemplateView

urlpatterns = [
    #front-end
     path('', HomeView.as_view(), name='home'),
    path('menus/', MenuHomeView.as_view(), name='menu_home'),
    path('login/', TemplateView.as_view(template_name="frontend/login.html"), name='login'),
]