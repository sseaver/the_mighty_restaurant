from django.contrib import admin
from app.models import Profile, Menu, Order, Table
# Register your models here.

admin.site.register([Profile, Menu, Order, Table])
