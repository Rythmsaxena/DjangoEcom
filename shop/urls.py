from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='shophome'),
    path('about/', views.about , name='about'),
    path('tracker/', views.tracker , name='tracker'),
    path('contact/', views.contact , name='contact'),
    path('search/', views.search , name='search'),
    path('productview/', views.productview , name='productview'),
    path('checkout/', views.checkout , name='checkout'),
]