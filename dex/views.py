from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Detail
from .forms import DetailForm

def detail_list(request):
    details = Detail.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'dex/detail_list.html', {'details': details})

def detail_detail(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    return render(request, 'dex/detail_detail.html', {'detail': detail})

def detail_new(request):
    if request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.author = request.user
            detail.published_date = timezone.now()
            detail.save()
            return redirect('detail_detail', pk=detail.pk)
    else:
        form = DetailForm()
    return render(request, 'dex/detail_edit.html', {'form': form})

def detail_edit(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    if request.method == "POST":
        form = DetailForm(request.POST, instance=detail)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.author = request.user
            detail.published_date = timezone.now()
            detail.save()
            return redirect('detail_detail', pk=detail.pk)
    else:
        form = DetailForm(instance=detail)
    return render(request, 'dex/detail_edit.html', {'form': form})