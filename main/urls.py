# main/urls.py

from django.urls import path
from .views import main_view, ipo_detail_view

urlpatterns = [
    path('', main_view, name='main_view'),
    path('ipo/<int:pk>/', ipo_detail_view, name='ipo_detail'),
]
