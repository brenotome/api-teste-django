from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

class User(AbstractBaseUser):
    username        = models.CharField(max_length=15,unique=True)
    email           = models.EmailField(unique=True)
    first_name      = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)
    address         = models.CharField(max_length=50)

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email,first_name,last_name']

    def __str__(self):
        return self.username

class Product(models.Model):
    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=200)
    price           = models.DecimalField(max_digits=6, decimal_places=2)
    creation_date   = models.DateField(auto_now=False, auto_now_add=False)
    stock           = models.IntegerField()
    
    def __str__(self):
        return self.name

class Order(models.Model):
    product         =models.ForeignKey(Product, on_delete=models.CASCADE)
    user            =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity        =models.IntegerField()
    total_price     =models.DecimalField(max_digits=6, decimal_places=2)
    paid            =models.BooleanField()

    def __str__(self):
        return self.product+self.user