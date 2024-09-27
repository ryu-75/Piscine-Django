from django.shortcuts import render, get_object_or_404
from .models import MarkdownContent

# base template
def html_render(request, slug):
    markdown_content = get_object_or_404(MarkdownContent, slug=slug)
    context = {"markdown_content": markdown_content}
    return render(request, 'ex01/base.html', context=context)

