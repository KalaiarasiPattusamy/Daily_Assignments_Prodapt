from django.db import models

# Create your models here.
class Seller(models.Model):
    sellername=models.CharField(max_length=50)
    sellerid=models.IntegerField()
    address=models.CharField(max_length=50)
    mobnum=models.BigIntegerField()
    