from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('buyer',views.buyers,name='buyer'),
    path('sellerform',views.selform,name='sellerform'),
    path('buyerform',views.buyform,name='buyerform'),
    path('seller',views.sellers,name='seller'),
    path('product',views.products,name='product'),
    path('dlt/<int:id>/',views.dlt,name='dlt'),
    path('update/<int:id>/',views.update,name='update'),
    path('formpro',views.formpro,name='formpro'),
    path('register',views.register,name='register'),
    path('signup',views.custom_creation,name='signup'),

]