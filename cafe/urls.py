from django.contrib import admin
from django.urls import path
from cafe import views

urlpatterns = [
    path("", views.index,name='home'),
    path("about", views.about,name='about'),
    path("product", views.product,name='product'),
    path("contact", views.contact,name='contact'),
    path("order", views.order,name='order'),
    path("recipt", views.recipt,name='recipt')
]