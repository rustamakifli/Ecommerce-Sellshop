
from django.template import Library
from blog.models import Blog

register = Library()


@register.simple_tag
def get_categories(offset, limit, order):
    if order > 0:
        return Blog.objects.all().order_by('created_at')[offset:limit]
    return Blog.objects.all().order_by('-created_at')[offset:limit]

@register.simple_tag
def related_categories(offset,limit):
    return Blog.objects.all().order_by('category')[offset:limit]