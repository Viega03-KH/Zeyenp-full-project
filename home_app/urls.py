from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('zeynep-about', views.about_page, name='about_page'),
    path('zeynep-contact', views.contact_page, name='contact_page'),
]