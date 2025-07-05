from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .models import Card, IPO
from .serializers import CardSerializer, IPOSerializer

# DRF API Views
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer

# HTML Detail View for individual IPO
def ipo_detail_view(request, pk):
    ipo = get_object_or_404(IPO, pk=pk)
    return render(request, 'ipo_detail.html', {'ipo': ipo})
