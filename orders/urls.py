from django.urls import path
from .views import CartView, CartItemDetail, OrderView

urlpatterns = [
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/<int:pk>/", CartItemDetail.as_view(), name="cart-detail"),
    path("", OrderView.as_view(), name="orders"),  # empty path, because included under api/orders/
]
