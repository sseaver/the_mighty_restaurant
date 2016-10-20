from django.shortcuts import render
from app.models import Menu, Order, Profile, Table
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['login_form'] = AuthenticationForm
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"
