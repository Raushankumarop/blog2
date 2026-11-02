import random
from django import template

register = template.Library()

@register.filter
def random_color(value):
    colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33F3', '#33FFF3']
    return random.choice(colors)