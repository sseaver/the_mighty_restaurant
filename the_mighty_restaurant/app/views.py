from django.shortcuts import render
from app.models import Menu, Order, Profile
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy

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
    success_url = "profile_view"


class ProfileView(UpdateView):
    template_name = "profile.html"
    fields = ("access_level",)
    success_url = reverse_lazy("profile_view")

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


class MenuItemCreateView(CreateView):
    model = Menu
    success_url = "/"
    fields = ("name", "description")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)


class OrderCreateView(CreateView):
    model = Order
    success_url = "/"
    fields = ("order", "table_number", "seat")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.server = self.request.user
        return super().form_valid(form)


class OrderUpdateView(UpdateView):
    model = Order
    success_url = "/"
    fields = ("order", "table_number", "seat")
