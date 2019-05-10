from django.shortcuts import render, get_object_or_404
from apartment.models import Apartment


def index(request):
    context = {'apartments': Apartment.objects.all().order_by('address')}
    return render(request, 'apartment/apartment-index.html', context)

# /apartment/1
def get_apartment_by_id(request, id):
    return render(request, 'apartment/apartment_details.html', {
        'apartment': get_object_or_404(Apartment, pk=id)
    })