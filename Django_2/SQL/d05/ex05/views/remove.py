from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ..models import Movies
from ..forms import RemoveForm

class Remove(View):
    def get(self, request):
        try:
            movies = Movies.objects.all().values()
            choices = [(movie['title'], movie['title']) for movie in movies]
            return render(request, 'ex05/remove.html', {'form': RemoveForm(choices=choices)})
        except Movies.DoesNotExist:
            return HttpResponse("No data available")
        
    def post(self, request):
        try:
            movies = Movies.objects.values('title')
            choices = [(movie['title'], movie['title']) for movie in movies]
            data = RemoveForm(choices, request.POST)
            if data.is_valid():
                Movies.objects.filter(title=data.cleaned_data['title']).delete()
                print(f'Data was correctly delete')
        except Movies.DoesNotExist:
            return HttpResponse('No data available')
        return redirect(request.path)