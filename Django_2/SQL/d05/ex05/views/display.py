from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from ..models import Movies

class   Display(View):
    def get(self, request):
        try:
            movies = Movies.objects.all().values()
            return render(request, 'ex05/display.html', {'movies': movies})
        except Movies.DoesNotExist as e:
            return HttpResponse(f"No data available : {e}")