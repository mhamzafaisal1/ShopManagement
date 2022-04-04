"""Defines URL patterns for shop_maangement_main."""

from django.urls import path

from . import views

app_name = 'shop_management_main'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Products page.
    path('products/', views.products, name='products'),
    #Adding new product page.
    path('new_product/', views.new_product, name='new_product'),
    #Transaction Page.
    path('transaction_days/', views.transaction_days, name='transaction_days'),
    # Individual transactions
    path('transactions/<int:transaction_day_id>/', views.transactions,
        name='transactions'),
    #url to add a new transaction Day
    path('new_transaction_day/', views.new_transaction_day,
        name='new_transaction_day'),
    #add new transaction.
    path('new_transaction/<int:transaction_day_id>/', views.new_transaction,
        name='new_transaction'),
    #Individual Product data.
    path('product_analysis/<int:product_id>/', views.p_summary, name='p_summary'),
]
