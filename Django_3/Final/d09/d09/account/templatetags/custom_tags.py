from django import template
from django.http import HttpRequest

register = template.Library()


@register.simple_tag
def get_user_picture(request: HttpRequest):
    if request.user.is_authenticated:
        if request.user.image.url is not None:
            print(request.user.image.url)
            return request.user.image.url
        else:
            return request.user.username[:1]
    return None


@register.simple_tag
def get_user_username(request: HttpRequest):
    if request.user.is_authenticated:
        return request.user.username
    return None


@register.simple_tag
def get_first_letter_username(request: HttpRequest):
    if request.user.is_authenticated:
        return request.user.username[0].capitalize()
    return ""
