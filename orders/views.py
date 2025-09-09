from rest_framework import generics, permissions
from .models import CartItem, Order
from .serializers import CartItemSerializer, OrderSerializer

class CartView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        cart_items = CartItem.objects.filter(user=self.request.user)
        total = sum([item.product.price * item.quantity for item in cart_items])
        order = serializer.save(user=self.request.user, total_price=total)
        order.products.set(cart_items)
        cart_items.delete()  # empty cart after order
