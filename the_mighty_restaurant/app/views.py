from django.shortcuts import render
from app.models import MenuItem, Order, Profile, Table
from app.forms import ChefOrderForm, ServerOrderForm
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
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
    success_url = "/"


class ProfileUpdateView(UpdateView):
    template_name = "profile_update.html"
    fields = ("access_level",)
    success_url = reverse_lazy("profile_update_view")

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


class MenuView(ListView):
    model = MenuItem
    template_name = "menu.html"


class MenuItemCreateView(CreateView):
    model = MenuItem
    success_url = "/"
    fields = ("name", "description", "price")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)


class MenuItemUpdateView(UpdateView):
    model = MenuItem
    success_url = reverse_lazy("menu_view")
    fields = ("name", "description", "price")


class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = "app/menuitem_delete.html"
    success_url = reverse_lazy("menu_view")

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return MenuItem.objects.all()
        return []


class OrderView(UpdateView):
    template_name = "orders.html"
    model = Order
    form_class = ChefOrderForm

    def get_queryset(self):
        return Order.objects.filter(completed=False)

    # def get_context_data(self, **kwargs):
    #     context = super(OrderView, self).get_context_data(**kwargs)
    #     context['table'] = Table.objects.get(id=self.kwargs['pk'])
    #     return context


class OrderCreateView(CreateView):
    model = Order
    success_url = reverse_lazy("table_view")
    form_class = ServerOrderForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.server = self.request.user
        instance.table = Table.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_object(self):
        return Table.objects.get(id=Table.id)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['table'] = Table.objects.get(id=self.kwargs['pk'])
    #     return context


class OrderUpdateView(UpdateView):
    model = Order
    success_url = reverse_lazy("table_view")
    form_class = ChefOrderForm


class TableView(ListView):
    model = Table
    template_name = "tables.html"

    def get_queryset(self):
        return Table.objects.filter(paid=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all()
        return context


class TableCreateView(CreateView):
    model = Table
    fields = ("table_number",)
    success_url = "/"


class OwnerView(ListView):
    model = Order
    template_name = "owner.html"
