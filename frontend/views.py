from django.views.generic import TemplateView
from menu.models import Menu
from order_management.models import Order
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # your login template
    success_url = reverse_lazy('home')  # your home page URL

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """If the user is already authenticated, redirect to the home page."""
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().form_valid(form)

class HomeView(TemplateView):
    template_name = "frontend/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Menu.objects.filter(specials=True)
        return context
    
class PaymentView(TemplateView):
    template_name = "frontend/payment.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(id=1)
        order_items = order.orderitem_set.all()  # get all OrderItem objects for the Order
        total_amount = sum(item.subtotal() for item in order_items)  # calculate the total amount
        context['total_amount'] = total_amount
        print(total_amount)
        return context
    
class OrderView(TemplateView):
    template_name = "frontend/orders.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all()
        return context
    
class AboutView(TemplateView):
    template_name = "frontend/about.html"

class FoodView(TemplateView):
    template_name = "frontend/foods.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Menu.objects.all()
        return context

@login_required
def profile(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user': user,
        'profile': profile,
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'frontend/profile.html', context)