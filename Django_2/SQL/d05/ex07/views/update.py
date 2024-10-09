from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Movies
from ..views import View
from ..forms import Form

class   Update(View):
    def get(self, request):
        try:
            movies = Movies.objects.all().values()
            choices = [(movie['title'], movie['title']) for movie in movies]
            return render(request, 'ex07/update.html', {'form': Form(choices=choices)})
        except Movies.DoesNotExist:
            return HttpResponse("No data available")
    
    def post(self, request):
        try:
            movies = Movies.objects.all().values()
            choices = [(movie['title'], movie['title']) for movie in movies]
        except Movies.DoesNotExist:
            return HttpResponse("No data available")
        
        form = Form(choices, request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            your_text = form.cleaned_data['your_text']
        try:
            movie = Movies.objects.get(title=title)
            movie.opening_crawl = your_text
            movie.save()
        except Movies.DoesNotExist:
            return HttpResponse("No data available")    
        return redirect(request.path)