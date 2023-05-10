from django.views.generic import ListView
from .models import Order, OrderItem
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Menu

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    

@csrf_exempt
def update_status(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print("***", data)
        orderId = data.get('orderId')
        status = data.get('newStatus')
        order = Order.objects.get(id=orderId)
        order.status = status
        order.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        
        data = json.loads(request.body.decode('utf-8'))
        item_id = data.get('id')
        quantity = int(data.get('qty'))
        address = data.get('address')
        name = data.get('name')
        price = float(data.get('price').strip().replace('$', ''))

        item = Menu.objects.get(id=item_id)
        
        # Create a new order or get the existing one for the customer
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, status=Order.WAITING)

        # Create or update the order item
        order_item, created = OrderItem.objects.get_or_create(order=order, menu_item=item)
        
        if not created:
            order_item.quantity += quantity
            order_item.save()

        # Calculate and save the total price for the order
        # order.calculate_total_price()
        order.save()
        print("saved****")
        # Check if the item is already in the cart, and update the quantity
        for cart_item in request.session.get('cart', []):
            if cart_item['id'] == item.id:
                cart_item['quantity'] += quantity
                cart_item['address'] = address
                request.session.modified = True
                return JsonResponse({'success': True})
        print("line 79***")
        # If the item is not in the cart, add it
        request.session.setdefault('cart', []).append({
            'id': item.id,
            'name': item.name,
            'price': price,
            'quantity': quantity,
            'address': address
        })
        print("line 88***")
        request.session.modified = True
        print("line 90***")
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})
