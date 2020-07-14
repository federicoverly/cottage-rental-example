from django.urls import path
from . import views

app_name='AppOne'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('address/', views.address, name='address'),
    path('gallery/', views.gallery, name='gallery'),
    path('nosotros/', views.nosotros, name='nosotros'),
]
