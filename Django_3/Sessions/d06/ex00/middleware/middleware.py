from datetime import datetime
from django.conf import settings
import random

class   MiddlewareAnonymeSessions():
    def __init__(self, get_response):
        self.get_response = get_response
        self.last_update = datetime.now().second
        
    def __call__(self, request):
        current_time = datetime.now().second
        new_time = current_time - self.last_update
        print(self.last_update)
        print(new_time)
        if new_time >= 5:
            name = settings.USERNAME
            request.session['name'] = random.choice(name)
            self.last_update = new_time
        response = self.get_response(request)
        
        return response