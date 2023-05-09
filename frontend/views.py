from django.views.generic import TemplateView
from menu.models import Menu
from math import ceil

class HomeView(TemplateView):
    template_name = "frontend/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Menu.objects.all()
        return context
