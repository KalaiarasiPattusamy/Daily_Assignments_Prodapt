from django.db import models

# Create your models here.
class Stock(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    manufacturer=models.CharField(max_length=50)
    rackno=models.IntegerField()
    quantity=models.IntegerField()
    price=models.IntegerField()
    
