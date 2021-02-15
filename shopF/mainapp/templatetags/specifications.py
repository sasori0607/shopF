from django import template

register = template.Library()

@register.filter
def products_spec(product):
    print(product)
    pass
