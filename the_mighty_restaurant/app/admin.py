from django.contrib import admin
from app.models import Profile, Menu, Order
# Register your models here.

admin.site.register([Profile, Menu, Order])
