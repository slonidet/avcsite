from django.shortcuts import render
from .models import Contacts, Structure
from content.models import Partners
# Create your views here.
def about(request):
    return render(request,"aboutassoc.html")

def structure(request):
    structure_sov = Structure.objects.filter(struc_soviet='sov').order_by('position')
    structure_dir = Structure.objects.filter(struc_soviet='dir').order_by('position')
    return render(request,"structure.html",{"sovets":structure_sov,"directors":structure_dir})

def contacts(request):
    contacts = Contacts.objects.get(id=1)
    return render(request, "contacts.html",{"contacts":contacts})

def partners(request):
    partners = Partners.objects.all().order_by('position')
    return render(request,"partners.html",{"partners":partners})