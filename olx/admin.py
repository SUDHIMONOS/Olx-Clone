from django.contrib import admin
from olx.models import Products,Brand,ProductImages,Notifications,Category

# Register your models here.
admin.site.register(Products)
admin.site.register(Brand)
admin.site.register(Notifications)
admin.site.register(Category)
admin.site.register(ProductImages)