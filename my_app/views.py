from django.shortcuts import render
from . models import Customer
def first_view(request):
    data = {
        'customers':Customer.objects.all()
    }
    return render(request, 'index.html', data)
