from django import forms
from app.models import Order


class ChefOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("completed",)


class ServerOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("item", "drink", "notes")
