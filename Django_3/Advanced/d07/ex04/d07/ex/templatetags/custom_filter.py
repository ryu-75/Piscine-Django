from django.utils import timezone
from django import template
from ex.models import User

register = template.Library()

@register.filter
def article_release_from(value):
    """
    Return the number of day from the release date to currently date
    """
    if not value:
        print("You should to added a valid date to get the correct number of day.")
    return (timezone.now() - value).days 

@register.inclusion_tag('login_form.html')
def login_context_form(**kwargs):
    username = kwargs['user']
    id = kwargs['id']
    form = User(username=username, id=id)
    return { 'login_form': form }