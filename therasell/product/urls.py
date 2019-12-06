from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
<<<<<<< HEAD
    path('list/new/', views.list_new, name='list_new'),
=======
    path('About_Us/', views.about_us, name = 'About_Us'),
    path('how_it_works/', views.how_it_works, name = 'how_it_works'),
>>>>>>> 276d5e64d5e9f43449382a9c1eb7bab4180cdc46
]