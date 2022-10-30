from django import template

register = template.Library()


# Calling cut() using decorator
@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

# Calling cut()
# register.filter('cut', cut)
