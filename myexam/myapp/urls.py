from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),  # Changed 'products/' to 'product/'.
    path('men/', views.men, name='men'),
     path('login/', views.login, name='login'),
]
