from django.urls import path
from . import views

urlpatterns = [

    path('', views.first, name='first'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('thank/', views.thank, name='thank'),
    path('detail/', views.detail, name='detail')
]