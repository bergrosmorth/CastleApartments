from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from apartment.models import Apartment
from profile.models import Profile
from django.contrib.auth import authenticate


# Create your views here.
def get_frontPage(request):
    import pdb; pdb.set_trace()
    context = {'apartments': Apartment.objects.all().order_by('address')}
    return render(request, 'login/login-index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            passwr = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=passwr)
            Profile(phone=0, user=user).save()
            return redirect('login')
    return render(request, 'login/register.html', {
        'form': UserCreationForm()
    })


def index(request):
    context = {'apartments': Apartment.objects.all().order_by('address')}
    return render(request, 'apartment/apartment-index.html', context)
