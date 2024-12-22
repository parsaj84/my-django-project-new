from django.db import models

class Category(models.Model):
    parent = models.ForeignKey("self" , verbose_name="parent" , blank=True,null=True, on_delete=models.CASCADE)
    categories = models.CharField(verbose_name= "category",blank=True,null=True,max_length=50)
    avatar = models.ImageField(verbose_name="avatar" ,blank=True,null=True,upload_to="media/")

    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"

class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category,blank=True)

    class Meta:
        db_table = "product"
        verbose_name = "product"
        verbose_name_plural = "products"


class File(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.FileField(verbose_name="file", upload_to="file/%Y/%m/%d/")

    class Meta:
        db_table = "file"
        verbose_name = "file"
        verbose_name_plural = "files"




    
# Create your models here.
