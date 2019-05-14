from django.shortcuts import render, get_object_or_404, redirect
from apartment.models import Apartment, ApartmentImage
from apartment.forms.apartment_form import ApartmentAddForm, ApartmentUpdateForm, BuyApartmentForm, BuyProfile
from django.http import JsonResponse


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        apartmentos = [{
            'id': x.id,
            'firstimage': x.apartmentimage_set.first().image,
            'address': x.address,
            'price': x.price
        } for x in Apartment.objects.filter(address__icontains=search_filter)]
        return JsonResponse({'data': apartmentos})
    context = {'apartments': Apartment.objects.all().order_by('address')}
    return render(request, 'apartment/apartment-index.html', context)

# /apartment/1
def get_apartment_by_id(request, id):
    return render(request, 'apartment/apartment_details.html', {
        'apartment': get_object_or_404(Apartment, pk=id)
    })

def add_apartment(request):
    if request.method == 'POST':
        form = ApartmentAddForm(data=request.POST)
        if form.is_valid():
            apartment = form.save(commit=False)
            apartment.realator = request.user
            apartment.save()
            apartment_image = ApartmentImage(image=request.POST['image'], apartment=apartment)
            apartment_image.save()
            return redirect('apartment-index')
    else:
        form = ApartmentAddForm()
    return render(request, 'apartment/add_apartment.html', {
        'form': form
    })

def delete_apartment(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    apartment.delete()
    return redirect('apartment-index')

def buy_apartment(request, id):
    house = Apartment.objects.get(pk=id)
    form = BuyApartmentForm(instance=house)
    if request.POST:
        return render(request, 'apartment/review_buyer.html',{
            'form': form,
            'apartment': get_object_or_404(Apartment, pk=id)
                      })
    return render(request, 'apartment/buy_apartment.html', {
        'form': form,
        'apartment': get_object_or_404(Apartment, pk=id)
    })

def update_apartment(request, id):
    instance = get_object_or_404(Apartment, pk=id)
    if request.method == "POST":
        form = ApartmentUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('apartment_details', id=id)
    else:
        form = ApartmentUpdateForm(instance=instance)
    return render(request, 'apartment/update_apartment.html', {
        'form': form,
        'id': id
    })


def payment_success(request):
    return render(request, 'apartment/payment_success.html')
