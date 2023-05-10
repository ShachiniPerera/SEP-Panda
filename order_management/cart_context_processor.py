from .models import OrderItem

def cart_items(request):
    cart_items = 0
    order_details_cart = None

    if request.user.is_authenticated:
        orders = OrderItem.objects.filter(order__customer=request.user, order__payment_verified=False)
        cart_items = orders.count()
        request.session['cart_items'] = cart_items
        order_details_cart = orders

    else:
        cart_items = request.session.get('cart_items', 0)

    print(type(order_details_cart))
    context = {
        'cart_items': cart_items,
        'order_details_cart': order_details_cart
    }

    return context