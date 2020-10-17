from django.shortcuts import render

from .models import Sighting

from django.shortcuts import get_object_or_404

from .forms import SightingRequestForm

from django.http import JsonResponse

def map_view(request):
    sightings = Sighting.objects.all()[:100]
    context={
            'sightings':sightings                            # To be revised
    }
    return render(request,'squirrel/map.html',context)

def list_all_sightings(request):
    sightings=Sighting.objects.all()
    context={
            'sightings':sightings                            # To be revised
    }
    return render(request,'squirrel/list_all_sightings.html',context)

def update_sighting(request,unique_squirrel_id):             #update the particular sight
    sighting = get_object_or_404(Squirrels, unique_squirrel_id=squirrel_id)
    form = Form(request.POST or None, instance=sighting)
    context = {'form': form}
    if form.is_valid():
        sighting = form.save(commit=False)
        sighting.save()
        return redirect('/sightings/')
    else:
        context = {
            'form': form,
        }
        return render(request, 'squirrel/update_form.html', context)

def create_sighting(request):
    if request.method=='POST':
        form = SightingRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = SightingRequestForm()
        context = {'form': form, }
        return render(request, 'squirrel/create_sighting.html', context)

def general_stats(request):
    sightings = Sighting.objects.all()

    total_number = sightings.count()
    count_black = sightings.filter(primary_fur_color='Black').count()
    count_running = sightings.filter(running='True').count()
    count_adult = sightings.filter(age='Adult').count()
    count_indifferent = sightings.filter(indifferent='True').count()

    context = {
            'total_number':total_number,
            'count_black':count_black,
            'count_running':count_running,
            'count_adult':count_adult,
            'count_indifferent':count_indifferent,
    }

    return render(request,'squirrel/stats.html',context)
    
# Create your views here.
