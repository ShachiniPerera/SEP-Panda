from django import template
from menu.models import Menu

register = template.Library()

@register.filter(name='query_by_id')
def query_by_id(queryset, id):
    return queryset.get(id=id)

@register.filter
def total_price(order_items):
    return f"${sum(item.menu_item.price * item.quantity for item in order_items):.2f}"

