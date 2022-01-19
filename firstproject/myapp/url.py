from django.urls import path

from myapp import views,admin

urlpatterns = [
    path('hii/',views.my,name="my"),
    path('',views.image,name="image")
]
