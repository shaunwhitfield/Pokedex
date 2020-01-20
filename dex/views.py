from django.shortcuts import render

def detail_list(request):
    return render(request, 'dex/detail_list.html', {})
