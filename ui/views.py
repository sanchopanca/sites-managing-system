from django.shortcuts import render, get_object_or_404

from .models import Site


def index(request):
    sites = Site.objects.all()
    return render(request, 'ui/index.html', {'sites': sites})


def site_entry(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    return render(request, 'ui/site-entry.html', {'site': site})


def summary(request):
    return render(request, 'ui/summary.html')


def summary_average(request):
    return render(request, 'ui/summary.html')
