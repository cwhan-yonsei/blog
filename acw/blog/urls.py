from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('model_test/', views.model_test, name='model_test'),
    path('', views.index, name='index'),
    path('article_list/<slug:tag>', views.article_list, name='article_list'),
    path('article/<int:pk>', views.article, name='article'),
    path('work_list/<slug:tag>', views.comming_soon, name='work_list'),
    path('about/', views.comming_soon, name='about'),
]