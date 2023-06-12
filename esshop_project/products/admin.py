from django.contrib import admin
from products.models import ProductCategory, Product, Basket


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category_id',)
    search_fields = ('name',)


class BasketInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp',)
    readonly_fields = ('created_timestamp',)
    extra = 0
