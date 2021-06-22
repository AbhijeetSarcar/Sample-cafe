from django.shortcuts import render
from .models import *
# Create your views here.

from django.shortcuts import render


# Create your views here.
def index(request):

    piz = pizza.objects.all()
    sal = salad.objects.all()
    nod = noodles.objects.all()
    return render(request, 'index.html', {'piz': piz, 'sal': sal, 'nod': nod})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
