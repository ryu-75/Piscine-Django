from django.shortcuts import render
from django.http import HttpResponse
from ..forms import Form
from ..models import Movies
from . import View

class   Display(View):
    def get(self, request):
        try :
            movies = Movies.objects.all().values()
            return render(request, 'ex07/display.html', {'movies': movies})
        except Movies.DoesNotExist:
            return HttpResponse("No data available")