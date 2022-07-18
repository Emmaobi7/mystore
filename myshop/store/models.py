from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    description = models.TextField()
    price = models.IntegerField()
    product_img = models.ImageField(upload_to='product_image')
    quauntity = models.IntegerField(default=0)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    top_selling = models.BooleanField(default=False)
    trandy = models.BooleanField(default=False)
    just_arrived = models.BooleanField(default=False)
    colour = models.CharField(max_length=20)
    size = models.IntegerField()

    def __str__(self):
        return self.category.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
   

class ProductSearch(models.Model):
    name_of_search = models.CharField(max_length=200)

    def __str__(self):
        return self.name_of_search
