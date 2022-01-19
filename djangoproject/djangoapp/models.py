from django.db import models

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=20)
    price=models.FloatField()
    details=models.TextField()
    def __str__(self):
        return self.product_name

class buyer(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.TextField()
    pro=models.ForeignKey(product,on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class seller(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.TextField()
    pro=models.ForeignKey(product,on_delete=models.CASCADE)
    def __str__(self):
        return self.name