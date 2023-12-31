from django.contrib import admin
from .models import Product, ProductPictures

class ProductAdmin(admin.ModelAdmin):
   list_display = ('name', 'type', 'price', 'stock')

class ProductPicturesAdmin(admin.ModelAdmin):
   list_display = ('product', 'priority', 'picture')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPictures, ProductPicturesAdmin)