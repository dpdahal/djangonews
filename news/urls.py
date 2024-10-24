from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.index),
    path('about',views.about),
    path('gallery/<page>',views.gallery),
]

