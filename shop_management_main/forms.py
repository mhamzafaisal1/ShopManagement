from django import forms
from .models import Product, Transaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['text', 'price', 'buy_price']
        labels = {
            'text'  : 'Enter product name',
            'price' : 'Enter selling price',
            'buy_price' : 'Enter purchase price'
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['product', 'quantity']
        labels = {
            'product' : 'Enter product',
            'quantity' : 'Enter quantity'
        }
    def __init__(self, user=None, **kwargs):
        super(TransactionForm, self).__init__(**kwargs)
        if user:
            self.fields['product'].queryset = (
                Product.objects.filter(owner=user)
            )
