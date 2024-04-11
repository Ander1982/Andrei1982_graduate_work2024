from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='works'),
    path('detail/<int:category_id>/', views.product, name='detail'),
    # path('products /<int:category_id>/', views.detail, name='product'),
    # path('<int:works_id>/', views.delete, name='delete'),

]