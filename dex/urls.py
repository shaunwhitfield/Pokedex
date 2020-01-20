from django.urls import path
from . import views

urlpatterns = [
    path('', views.detail_list, name='detail_list'),
    path('detail/<int:pk>/', views.detail_detail, name='detail_detail'),
    path('detail/new/', views.detail_new, name='detail_new'),
    path('detail/<int:pk>/edit/', views.detail_edit, name='detail_edit'),
]