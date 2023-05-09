from django import template
from menu.models import Menu

register = template.Library()

@register.filter(name='query_by_id')
def query_by_id(queryset, id):
    return queryset.get(id=id)