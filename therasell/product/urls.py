from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('list/new/', views.list_new, name='list_new'),
    path('About_Us/', views.about_us, name = 'About_Us'),
    path('how_it_works/', views.how_it_works, name = 'how_it_works'),
    path('Checkout/', views.checkout, name = 'checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)