from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import AnnouncedPUResults, PollingUnit, LGA,AnnouncedLGAResults

# Create your views here.
def home(request):
    return render(request, 'home.html')

def polling_unit_results(request, polling_unit_id):
    results = AnnouncedLGAResults.objects.filter(lga_name=polling_unit_id)
    return render(request, 'polling_unit_results.html', {'results': results})

def lga_results(request):
    lgas = LGA.objects.all()
    results = []

    if request.method == 'POST':
        lga_id = request.POST.get('lga_id')
        polling_units = PollingUnit.objects.filter(lga_id=lga_id)
        results = AnnouncedPUResults.objects.filter(polling_unit_uniqueid__in=polling_units)
    
    return render(request, 'lga_results.html', {'lgas': lgas, 'results': results})

def add_results(request):
    if request.method == 'POST':
        polling_unit_id = request.POST['polling_unit_id']
        party_scores = request.POST.getlist('party_scores')

        for party_score in party_scores:
            party, score = party_score.split(':')
            AnnouncedPUResults.objects.create(
                polling_unit_uniqueid=polling_unit_id,
                party_abbreviation=party,
                party_score=int(score)
            )
        return HttpResponseRedirect('/success/')
    
    return render(request, 'add_results.html')

def success(request):
    return render(request, 'success.html')  # Make sure you have a success.html template