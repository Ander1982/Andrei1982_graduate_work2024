from django.urls import path
from . import views

urlpatterns = [
    path('', views.works, name='works'),
    path('<int:works_id>/', views.detail, name='detail'),
    path('<int:works_id>/', views.delete, name='delete'),

]