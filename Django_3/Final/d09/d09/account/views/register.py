from django.http import JsonResponse
from typing import Any, Dict
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from account.forms import RegisterForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin


class RegisterView(UserPassesTestMixin, FormView):
    template_name = "form.html"
    form_class = RegisterForm
    success_url = reverse_lazy("index")

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["action"] = "register"
        context["title"] = "Register"
        return context

    def form_valid(self, form: RegisterForm) -> JsonResponse:
        user = form.record_data()
        login(self.request, user)
        messages.success(self.request, "User registered successfully")
        return JsonResponse({"redirect_url": str(self.success_url)}, status=200)

    def form_invalid(self, form: RegisterForm) -> JsonResponse:
        messages.warning(self.request, "Registration failed.")
        return JsonResponse({"errors": form.errors}, status=400)
