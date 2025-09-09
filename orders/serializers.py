from rest_framework import serializers
from .models import CartItem, Order
from products.models import Product  # ✅ Import added

class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity']

    def get_product(self, obj):
        return {
            "id": obj.product.id,
            "title": obj.product.title,
            "price": obj.product.price
        }

class OrderSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(many=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'total_price', 'status', 'created_at']
