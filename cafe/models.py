from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    message= models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=122)
    image= models.CharField(max_length=122)
    witha= models.CharField(max_length=122)
    price= models.CharField(max_length=10)


class Order(models.Model):
    oid = models.IntegerField(primary_key=True)
    noc = models.CharField(max_length=122)
    cardno = models.CharField(max_length=20)
    expiry = models.CharField(max_length=20)
    prod= models.CharField(max_length=50)
    price =models.CharField(max_length=10)
    cvv = models.CharField(max_length=4)
    street = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    zip = models.CharField(max_length=6)

class Rder(models.Model):
    oid = models.AutoField(primary_key=True)
    noc = models.CharField(max_length=122)
    cardno = models.CharField(max_length=20)
    expiry = models.CharField(max_length=20)
    prod= models.CharField(max_length=50)
    price =models.CharField(max_length=10,default="", editable=False)
    cvv = models.CharField(max_length=4)
    street = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    zip = models.CharField(max_length=6)

class Ct(models.Model):
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    message= models.TextField()
