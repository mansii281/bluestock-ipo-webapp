from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CardViewSet, IPOViewSet
from . import views

router = DefaultRouter()
router.register(r'card', CardViewSet)
router.register(r'ipo', IPOViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ipo-detail/<int:pk>/', views.ipo_detail_view, name='ipo_detail'),  # 👈 Add this
]
