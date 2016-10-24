"""the_mighty_restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app.views import IndexView, UserCreateView, ProfileUpdateView, OrderCreateView,  \
                      MenuItemCreateView, OrderUpdateView, MenuItemUpdateView, \
                      MenuView, MenuItemDeleteView, OrderView, TableView, TableCreateView, \
                      OwnerView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^profile/update/$', ProfileUpdateView.as_view(), name="profile_update_view"),
    url(r'^orders/$', OrderView.as_view(), name="order_view"),
    url(r'^tables/(?P<pk>\d+)/orders/create/$', OrderCreateView.as_view(), name="order_create_view"),
    url(r'^order/(?P<pk>\d+)/update/$', OrderUpdateView.as_view(), name="order_update_view"),
    url(r'^menu/$', MenuView.as_view(), name="menu_view"),
    url(r'^menu_item/create/$', MenuItemCreateView.as_view(), name="menu_item_create_view"),
    url(r'^menu_item/(?P<pk>\d+)/update/$', MenuItemUpdateView.as_view(), name="menu_item_update_view"),
    url(r'^menu_item/(?P<pk>\d+)/delete/$', MenuItemDeleteView.as_view(), name="menu_item_delete_view"),
    url(r'^tables/$', TableView.as_view(), name="table_view"),
    url(r'^create_table/$', TableCreateView.as_view(), name="table_create_view"),
    url(r'^owner/$', OwnerView.as_view(), name="owner_view")
]
