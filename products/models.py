from django.db import models
from users.models import User

# Create your models here.

class Category(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # ✅ use Category
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    wishlisted_by=models.ManyToManyField('users.User',related_name='wishlist',blank=True)

    def __str__(self):
        return self.title
