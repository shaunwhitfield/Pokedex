from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Detail

def detail_list(request):
    details = Detail.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'dex/detail_list.html', {'details': details})

def detail_detail(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    return render(request, 'dex/detail_detail.html', {'detail': detail})
