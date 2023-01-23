from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile=models.ImageField(null=True,upload_to="profile.images")
    address=models.CharField(max_length=300)
    phone=models.PositiveIntegerField()

    
    def __str__(self):
        return self.user

class Products(models.Model):
    name=models.CharField(max_length=200)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    condition=models.CharField(max_length=50, null=True)
    category=models.ForeignKey("Category",on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    Options=(
        ("for-sale","for-sale"),
        ("exchange","exchange"),
        ("rent","rent")
    )
    status=models.CharField(max_length=30, choices=Options,default="for-sale")
    created_date=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

class Category(models.Model):
        category_name=models.CharField(max_length=100)
        is_activate=models.BooleanField(default=True)


        def __str__(self):
            return self.category_name


class Brand(models.Model):
    brand_name=models.CharField(max_length=100)

    def __str__(self):
            return self.brand_name


class ProductImages(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    image=models.ImageField(null=True,upload_to="product.images")


    def __str__(self):
            return self.product

class Notifications(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    buyer=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    Options=(
        ("sent","sent"),
        ("pending","pending"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=50,choices=Options)


    def __str__(self):
        return self.product





