from django.urls import path
from . import views

urlpatterns = [
    path('', views.detail_list, name='detail_list'),
    path('detail/<int:pk>/', views.detail_detail, name='detail_detail'),
]