from django.urls import path
from . import views

urlpatterns = [
    path('zeynep-gallery', views.gallery_page, name='gallery_page'),
    path('zeynep-single/<int:id>/', views.single_page, name='single_page'),
    path('zeynep-collection', views.collection_page, name='collection_page'),
]
