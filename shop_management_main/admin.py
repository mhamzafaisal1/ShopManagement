from django.contrib import admin
from .models import Product, Transaction, TransactionDay

admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(TransactionDay)
