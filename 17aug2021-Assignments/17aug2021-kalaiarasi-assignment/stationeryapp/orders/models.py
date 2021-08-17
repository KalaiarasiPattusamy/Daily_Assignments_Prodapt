from django.db import models

# Create your models here.
class Order(models.Model):
    itemname=models.CharField(max_length=50)
    count=models.IntegerField()
    
    
    
