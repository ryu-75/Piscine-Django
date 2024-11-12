from django import template
from datetime import datetime
from django.utils import timezone
register = template.Library()

@register.filter
def article_release_from(value):
    if not value:
        return ""
    
    now = timezone.now()
    delta = now - value
    
    days = delta.days
    months = days // 30
    weeks = (days % 30) // 7
    days = days % 7
    
    duration_parts = []
    if months > 0:
        duration_parts.append(f"{months} month{'s' if months > 1 else ''}")
    if weeks > 0:
        duration_parts.append(f"{weeks} week{'s' if weeks > 1 else ''}")
    if days > 0:
        duration_parts.append(f"{days} day{'s' if days > 1 else ''}")
        
    return ", ".join(duration_parts) if duration_parts else "today"