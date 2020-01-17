from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('model_test/', views.model_test, name='model_test'),
    path('article_list/<slug:tag>', views.article_list, name='article_list'),
    path('', views.index),
    path('article/<int:pk>', views.article, name='article'),
]