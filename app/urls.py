from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('supplier/', supplier, name='supplier'),
    path('purchase/', purchase, name = 'purchase'),
    path('purchaseInfo/', poNumberData, name = 'info'),
    path('submit/', submit, name = 'submit'),

]
