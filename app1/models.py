from django.db import models

# Create your models here.

class customer(models.Model):
     username = models.CharField(max_length=100, primary_key=True)
     useraddress = models.TextField()

class fooditem(models.Model):
     foodname = models.CharField(max_length=100)
     foodprice = models.IntegerField()
     def __str__(self):
          return self.foodname

class reviews(models.Model):
     foodid = models.ForeignKey(fooditem, on_delete=models.CASCADE)
     cutomername = models.ForeignKey(customer, on_delete=models.CASCADE)
     rating = models.IntegerField()