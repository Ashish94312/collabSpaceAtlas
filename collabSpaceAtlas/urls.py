from django.urls import path
from . import views

urlpatterns = [
    path('', views.content_list, name='content-list'),
    path('content/', views.content_list, name='content-list'),
    path('content/<slug:slug>/', views.content_view, name='content-view'),
]
