from django.urls import path
from . import views

urlpatterns = [
    path('', views.store , name = 'store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('search/', views.search, name = 'search'),

    path('update_item/', views.updateItem, name='update_item'),
]