from django.shortcuts import render

def display(request):
    return render(request, 'ex01/display.html')

def templates(request):
    return render(request, 'ex01/templates.html')

def django(request):
    return render(request, 'ex01/django.html')