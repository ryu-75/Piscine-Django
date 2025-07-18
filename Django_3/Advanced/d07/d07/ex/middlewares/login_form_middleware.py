from django.utils.deprecation import MiddlewareMixin
from ex.forms import LoginForm
from django.http import HttpRequest, HttpResponse

class LoginFormMiddleware(MiddlewareMixin):
    def process_template_response(self, request: HttpRequest, response: HttpResponse):
        response.context_data['login_form'] = LoginForm
        return response