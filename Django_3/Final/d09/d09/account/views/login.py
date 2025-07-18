from django.views.generic import View
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from account.forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin


class LoginView(UserPassesTestMixin, View):
    template_name = "form.html"
    form_class = LoginForm
    success_url = reverse_lazy("index")

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return HttpResponseRedirect(self.success_url)

    def get(self, request: HttpRequest) -> HttpResponse:
        """Render the login form."""
        form = self.form_class()
        context = {"title": "Login", "form": form, "action": "login"}
        return render(request, self.template_name, context=context)

    def post(self, request: HttpRequest) -> JsonResponse | HttpResponse:
        """Handle POST request to treat the login"""
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                if user and user.is_active:
                    login(request, user)
                    messages.success(request, "You are logged in now!")
                    return JsonResponse(
                        {"redirect_url": str(self.success_url)}, status=200
                    )
                return JsonResponse({"errors": "Inactive profile"}, status=400)
            else:
                return JsonResponse({"errors": form.errors}, status=400)
        else:
            form = AuthenticationForm()
        return HttpResponseRedirect(self.success_url)
