from django.db import models


class Category(models.Model):
    """
    Model representing a category for products.
    """

    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """
    Model representing a product.
    """

    name = models.CharField(max_length=255)
    photo = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    offer_of_the_month = models.BooleanField(default=False)
    availability = models.BooleanField(default=False)
    pickup = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Description(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
