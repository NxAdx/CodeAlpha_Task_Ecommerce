from django.urls import path
from .views import (
    ItemDetailView,
    Base,
    HomeView,
    add_to_cart,
    CheckoutView,
    remove_from_cart,
    OrderSummary,
    remove_single_from_cart,
    PaymentView
)

app_name = 'core'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('order-summary/', OrderSummary.as_view(), name='order-summary'),
    path('check/', CheckoutView.as_view(), name='checkout'),
    path('base/', Base, name='checkout'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('payment/<payment_option>', PaymentView.as_view(), name='payment'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-from-cart/<slug>/',
         remove_single_from_cart, name='remove-single-from-cart'),


]
