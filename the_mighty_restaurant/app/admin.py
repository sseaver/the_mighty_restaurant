from django.contrib import admin
from app.models import Profile, MenuItem, Order
# Register your models here.

admin.site.register([Profile, MenuItem, Order])
