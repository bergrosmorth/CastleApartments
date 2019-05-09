from django.shortcuts import render
from customer.models import Customer

# Create your views here.
def index(request):
    context = {'customers': 'hello'}
    return render(request, 'customer/customer-index.html', context)