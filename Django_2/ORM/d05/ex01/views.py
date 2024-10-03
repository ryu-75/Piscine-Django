from django.shortcuts import render

def ex01(request):
    return render(request, 'ex01/index.html')
