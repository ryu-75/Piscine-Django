from django.shortcuts import render
import json, os
from django.conf import settings


def array(request):
    json_path = os.path.join(settings.BASE_DIR, 'ex03/static/json/onepiece.json')
    with open(json_path, 'r') as f:
        data = json.load(f)
    context = {'data': data['members']}
    return render(request, 'ex03/array.html', context)
