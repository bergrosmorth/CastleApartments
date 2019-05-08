from django.shortcuts import render
from apartment.models import Apartment

# Create your views here.
def index(request):
    return render(request, 'apartment/apartment-index.html')

def get_apartments(request):
    context = {'apartments': Apartment.objects.all().order_by('id')}
    return render(request, 'apartment/apartments.html', context)