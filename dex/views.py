from django.shortcuts import render
from django.utils import timezone
from .models import Detail

def detail_list(request):
    details = Detail.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'dex/detail_list.html', {'details': details})
