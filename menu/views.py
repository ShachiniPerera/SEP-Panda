from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Ingredient, Category, Menu
from .forms import IngredientForm, CategoryForm, MenuForm

class MenuHomeView(TemplateView):
    template_name = "menu/home.html"

class IngredientListView(ListView):
    model = Ingredient

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy('ingredient_list')

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy('ingredient_list')

class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy('ingredient_list')

class CategoryListView(ListView):
    model = Category

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')

class MenuListView(ListView):
    model = Menu

class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    success_url = reverse_lazy('menu_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['ingredients'] = Ingredient.objects.all()
        return context

class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    success_url = reverse_lazy('menu_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['ingredients'] = Ingredient.objects.all()
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy('menu_list')

class DashboardView(TemplateView):
    template_name = "dashboard.html"