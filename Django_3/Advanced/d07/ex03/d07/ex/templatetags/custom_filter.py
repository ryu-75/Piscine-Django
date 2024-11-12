from django.utils import timezone
from django import template

register = template.Library()

@register.filter
def article_release_from(value):
    """
    Return the number of day from the release date to currently date
    """
    if not value:
        print("You should to added a valid date to get the correct number of day.")
    return (timezone.now - value).days 