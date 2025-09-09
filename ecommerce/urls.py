from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),       # users API
    path('api/products/', include('products.urls')), # products API
    path('api/orders/', include('orders.urls')),
    path('api/', include('reviews.urls')),
    path('api/', include('notification.urls')),
    path('api/', include('wishlist.urls')),


    # orders & cart API
]
