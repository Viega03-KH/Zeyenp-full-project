from django.urls import path
from . import views

urlpatterns = [
    path('zeynep-news', views.news_page, name='news_page'),
    path('zeynep-news-single/<int:id>', views.news_single_page, name='news_single_page'),
]
