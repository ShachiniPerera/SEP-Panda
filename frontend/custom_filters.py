from django import template

register = template.Library()

@register.filter
def total_price(order_details_cart):
    total = sum(item['subtotal'] for item in order_details_cart)
    return f"${total:.2f}"
