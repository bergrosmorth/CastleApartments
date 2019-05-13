from django.forms import ModelForm, widgets
from django import forms
from apartment.models import Apartment

class ApartmentAddForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'})), fá margar myndir virkar ekki
    class Meta:
        model = Apartment
        exclude = [ 'id', 'realator']
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

<<<<<<< HEAD
class BuyApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = [ 'id', 'realator']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'SSN': widgets.NumberInput(attrs={'class': 'form-control'}),
            'card number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expiration date': widgets.NumberInput(attrs={'class': 'form-control'}),
            'CVC': widgets.TextInput(attrs={'class': 'form-control'}),
=======
class ApartmentUpdateForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ['id', 'realator']
        widgets = {
            'address': widgets.TextInput( attrs={'class': 'form-control'} ),
            'zip': widgets.TextInput( attrs={'class': 'form-control'} ),
            'city': widgets.TextInput( attrs={'class': 'form-control'} ),
            'country': widgets.Select( attrs={'class': 'form-control'} ),
            'size': widgets.NumberInput( attrs={'class': 'form-control'} ),
            'price': widgets.NumberInput( attrs={'class': 'form-control'} ),
            'rooms': widgets.NumberInput( attrs={'class': 'form-control'} ),
            'description': widgets.TextInput( attrs={'class': 'form-control'} ),
>>>>>>> 2dcf5707027fbec23cdb50e208103f1a831ca8c1
        }