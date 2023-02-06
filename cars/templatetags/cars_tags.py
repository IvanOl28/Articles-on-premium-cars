from django import template
from cars.models import *

register = template.Library() #создаем экз класса, через к-1 происходит регистация собстенный шаблонов-тэгов


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('cars/list_categories.html') #шаблон будет вогвращаться тэгом в базовом шаблоне
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected} #предается шаблону list_categories.html
