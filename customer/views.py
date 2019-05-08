from django.shortcuts import render
from customer.models import Customer

# Create your views here.
def index(request):
    context = {'customers': Customer.objects.all().order_by('name')}
    return render(request, 'customer/customer-index.html', context)