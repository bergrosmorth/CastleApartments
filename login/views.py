from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from apartment.models import Apartment


# Create your views here.
def get_frontPage(request):
    context = {'apartments': Apartment.objects.all().order_by('address')}
    return render(request, 'login/login-index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'login/register.html', {
        'form': UserCreationForm()
    })


def index(request):
    context = {'apartments': Apartment.objects.all().order_by('address')}
    return render(request, 'apartment/apartment-index.html', context)