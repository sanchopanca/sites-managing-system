from django.db.models import Avg
from django.shortcuts import render, get_object_or_404

from .models import Site


def index(request):
    sites = Site.objects.all()
    return render(request, 'ui/index.html', {'sites': sites})


def site_entry(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    return render(request, 'ui/site-entry.html', {'site': site})


def summary(request):
    sites = Site.objects.all()
    for site in sites:
        entries = site.statistics_entries.all()
        site.aggregation_a = sum(entry.a for entry in entries)
        site.aggregation_b = sum(entry.b for entry in entries)
    return render(request, 'ui/summary.html', {'sites': sites})


def summary_average(request):
    sites = Site.objects.annotate(aggregation_a=Avg('statistics_entries__a'),
                                  aggregation_b=Avg('statistics_entries__b'))
    return render(request, 'ui/summary.html', {'sites': sites})
