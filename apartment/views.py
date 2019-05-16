from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from apartment.models import Apartment, ApartmentImage
from apartment.forms.apartment_form import ApartmentAddForm, ApartmentUpdateForm, BuyApartmentForm, \
    BuyerInformationForm, ApartmentImageForm
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import json as simplejson


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

    if 'range_filter' in request.GET:
        price = request.GET.get('price')
        size = request.GET.get('size')
        rooms = request.GET.get('rooms')
        zip = request.GET.get('zip')
        apartmentos = [{
            'id': x.id,
            'firstimage': x.apartmentimage_set.first().image,
            'address': x.address,
            'price': x.price,
            'size': x.size,
            'rooms': x.rooms,
            'zip': x.zip
        } for x in Apartment.objects.filter(price__range=(0, price))]
        return JsonResponse({'data': apartmentos})

    '''elif 'price_filter' in request.GET:
        price_filter = request.GET['price_filter']
        apartmentos = [{
            'id': x.id,
            'firstimage': x.apartmentimage_set.first().image,
            'address': x.address,
            'price': x.price
        } for x in Apartment.objects.filter(price__range=(0, price_filter))]
        return JsonResponse({'data': apartmentos})

    elif 'size_filter' in request.GET:
        size_filter = request.GET['size_filter']
        apartmentos = [{
            'id': x.id,
            'firstimage': x.apartmentimage_set.first().image,
            'size': x.size,
            'address': x.address,
            'price': x.price
        } for x in Apartment.objects.filter(size__range=(0, size_filter))]
        return JsonResponse({'data': apartmentos})

    elif 'room_filter' in request.GET:
        room_filter = request.GET['room_filter']
        apartmentos = [{
            'id': x.id,
            'firstimage': x.apartmentimage_set.first().image,
            'rooms': x.rooms,
            'address': x.address,
            'price': x.price
        } for x in Apartment.objects.filter(rooms__range=(0, room_filter))]
        return JsonResponse({'data': apartmentos})

    elif 'zip_filter' in request.GET:
        zip_filter = request.GET['zip_filter']
        apartmentos = [{
            'id': x.id,
            'firstimage': x.apartmentimage_set.first().image,
            'zip': x.zip,
            'address': x.address,
            'price': x.price
        } for x in Apartment.objects.filter(zip__exact=zip_filter)]
        return JsonResponse({'data': apartmentos})'''
    context = {'apartments': Apartment.objects.all().order_by('address')}
    return render(request, 'apartment/apartment-index.html', context)


# /apartment/1
def get_apartment_by_id(request, id):
    return render(request, 'apartment/apartment_details.html', {
        'apartment': get_object_or_404(Apartment, pk=id)})

@login_required
def add_apartment(request):

    ImageFormSet = modelformset_factory(ApartmentImage, form=ApartmentImageForm, extra=6, max_num=6)

    if request.method == 'POST':
        apartment_form = ApartmentAddForm(data=request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=ApartmentImage.objects.none())

        if apartment_form.is_valid() and image_formset.is_valid():

            apartment = apartment_form.save(commit=False)
            apartment.realator = request.user
            apartment.save()

            images = image_formset.save(commit=False)

            for image in images:
                image.apartment = apartment
                image.save()

            return redirect('apartment-index')
        else:
            return render(request, 'apartment/add_apartment.html', {
                'form': apartment_form, 'formset': image_formset})
    else:
        apartment_form = ApartmentAddForm()
        image_formset = ImageFormSet(queryset=ApartmentImage.objects.none())
        return render(request, 'apartment/add_apartment.html', {
            'form': apartment_form, 'formset': image_formset})


def delete_apartment(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    apartment.delete()
    return redirect('apartment-index')


def buy_apartment(request, id):
    house = Apartment.objects.get(pk=id)
    form = BuyApartmentForm()
    buyer = BuyerInformationForm()
    if request.POST:
        buyer = BuyerInformationForm(data=request.POST)
        if buyer.is_valid():
            b = buyer.save(commit=False)
            b.user = request.user
            b.apartment = house
            b.save()
            return render(request, 'apartment/payment_success.html')
    return render(request, 'apartment/buy_apartment.html', {
        'form': form,
        'bform': buyer,
        'apartment': get_object_or_404(Apartment, pk=id)})


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
        'id': id})


def payment_success(request):
    return render(request, 'apartment/payment_success.html')


