from django.shortcuts import render


def index(request):
    return render(request, 'ui/index.html')


def site_entry(request):
    return render(request, 'ui/site-entry.html')


def summary(request):
    return render(request, 'ui/summary.html')


def summary_average(request):
    return render(request, 'ui/summary.html')
