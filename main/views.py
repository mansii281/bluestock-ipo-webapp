# main/views.py

from django.shortcuts import render, get_object_or_404
from cardapi.models import IPO

def main_view(request):
    ipos = IPO.objects.all()
    return render(request, 'home.html', {'ipos': ipos})

def ipo_detail_view(request, pk):
    ipo = get_object_or_404(IPO, pk=pk)
    return render(request, 'ipo_detail.html', {'ipo': ipo})
