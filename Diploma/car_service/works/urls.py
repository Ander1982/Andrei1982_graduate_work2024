from django.urls import path
from . import views

urlpatterns = [
    path('', views.works, name='works'),
    # path('<int:blog_id>/', views.detail, name='detail'),

]