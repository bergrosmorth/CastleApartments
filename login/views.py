from django.shortcuts import render

# Create your views here.
def get_frontPage(request):
    return render(request, 'login/login-index.html')