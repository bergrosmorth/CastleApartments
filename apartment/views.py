from django.shortcuts import render
from apartment.models import Apartment


def index(request):
    context = {'apartments': Apartment.objects.all().order_by('address')}
    return render(request, 'apartment/apartment-index.html', context)