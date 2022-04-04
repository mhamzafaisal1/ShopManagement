from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    """Products the shopkeeper sells in his shop"""
    text       = models.CharField(max_length=50)
    price      = models.DecimalField(max_digits=8, decimal_places=2)
    buy_price  = models.DecimalField(max_digits=8, decimal_places=2)
    owner      = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return the string representation of the model."""
        return self.text

    class Meta:
        ordering = ['text']    

class TransactionDay(models.Model):
    """Table to store transactions on a single day"""
    owner  = models.ForeignKey(User, on_delete=models.CASCADE)
    date   = models.DateField(auto_now_add=True)
    sum    = models.DecimalField(max_digits=12, decimal_places=2)
    profit = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        """Return the string representation of the model."""
        return str(self.date)

class Transaction(models.Model):
    """Table to represent all transactions occured on a day"""
    day      = models.ForeignKey(TransactionDay, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=1)

    def __str__(self):
        """Return the string representation of the model."""
        return str(self.product)
