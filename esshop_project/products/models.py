from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Category name', max_length=64, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Products Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True)
    short_decription = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} | {self.category_id.name}'
