from django.forms import ModelForm, widgets
from django import forms
from apartment.models import Apartment, BuyerInformation, ApartmentImage
from profile.models import Profile


class ApartmentAddForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ['id', 'realator']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class BuyApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = [ 'id', 'realator', 'price', 'size', 'rooms', 'description']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
        }

class BuyerInformationForm(ModelForm):
    class Meta:
        model = BuyerInformation
        exclude = ['id', 'user', 'apartment']
        widgets = {
            'ssn': widgets.TextInput(attrs={'class': 'form-control'}),
            'cardnumber': widgets.TextInput(attrs={'class': 'form-control'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control'}),
            'month':widgets.TextInput(attrs={'class': 'form-control'}),
            'year': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class BuyProfile(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id']

class ApartmentUpdateForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ['id', 'realator']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
        }

#class SharingForms(forms.Form):
#    photos = forms.ImageField()

class ApartmentImageForm(ModelForm):
    class Meta:
        model = ApartmentImage
        exclude = ['id', 'apartment']