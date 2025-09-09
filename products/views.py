from rest_framework import viewsets, permissions, filters

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'stock']

    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions


class ProductViewset(viewsets.ModelViewSet):
    ...
    @action(detail=True, methods=['POST'], permission_classes=[permissions.IsAuthenticated])
    def add_to_wishlist(self, request, pk=None):
        product = self.get_object()
        product.wishlisted_by.add(request.user)
        return Response({'status': 'added to wishlist'})

    @action(detail=True, methods=['POST'], permission_classes=[permissions.IsAuthenticated])
    def remove_from_wishlist(self, request, pk=None):
        product = self.get_object()
        product.wishlisted_by.remove(request.user)
        return Response({'status': 'removed from wishlist'})
