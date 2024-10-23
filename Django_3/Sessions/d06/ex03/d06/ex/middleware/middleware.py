import time
from django.conf import settings
import random
from django.http import HttpRequest
from  django.utils.deprecation import MiddlewareMixin 

SESSION_TIME_EXPIRE = 42
class   MiddlewareAnonymeSessions(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        if request.user.is_authenticated:
            return
        current_time = time.time()
        init_time = request.session.setdefault('anonymous_timestamp', current_time)
        if time.time() - init_time > SESSION_TIME_EXPIRE:
            request.session.flush()
        if 'anonymous' not in request.session:
            request.session['anonymous'] = random.choice(settings.USERNAME)
            request.session['anonymous_timestamp'] = current_time