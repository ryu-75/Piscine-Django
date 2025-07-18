from typing import Any, Dict
from django.views.generic.edit import FormView
from ex.forms import LoginForm
from django.contrib.auth import login
from django.shortcuts import HttpResponseRedirect
from django.http import HttpRequest
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate


class Login(FormView):
    template_name = "articles/articles.html"
    form_class = LoginForm
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            messages.error(self.request, "You're already connected")
            return HttpResponseRedirect(self.success_url)
        return super().get(request)

    def get_context_data(self, **kwargs: Dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.LANGUAGE_CODE == "en":
            context["link"] = "login"
            context["btn_name"] = "Sign in"
        else:
            context["link"] = "connexion"
            context["btn_name"] = "Se connecter"
        return context

    def form_valid(self, form: LoginForm):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.info(self.request, "You are now logged")
            return HttpResponseRedirect(self.success_url)
        return self.form_invalid(form)

    def form_invalid(self, form: LoginForm):
        return self.render_to_response(self.get_context_data(form=form))
