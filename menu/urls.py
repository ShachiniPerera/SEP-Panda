from django.urls import path
from .views import (
    IngredientListView, IngredientCreateView, IngredientUpdateView, IngredientDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    MenuListView, MenuCreateView, MenuUpdateView, MenuDeleteView, DashboardView
)

urlpatterns = [
    # Ingredient URLs
    path('ingredients', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/create', IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredients/<int:pk>/update', IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredients/<int:pk>/delete', IngredientDeleteView.as_view(), name='ingredient_delete'),
    
    # Category URLs
    path('categories', CategoryListView.as_view(), name='category_list'),
    path('categories/create', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete', CategoryDeleteView.as_view(), name='category_delete'),
    
    # Menu URLs
    path('menus', MenuListView.as_view(), name='menu_list'),
    path('menus/create', MenuCreateView.as_view(), name='menu_create'),
    path('menus/update/<int:pk>/', MenuUpdateView.as_view(), name='menu_update'),
    path('menus/delete/<int:pk>/', MenuDeleteView.as_view(), name='menu_delete'),
    
    path('', DashboardView.as_view(), name='dashboard'),
]