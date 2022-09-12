from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
data_katalog_item = CatalogItem.objects.all()
context = {
    'list_barang': data_katalog_item,
    'nama': 'Fadlan Ariel Fathurrahman',
    'npm' : '2106750673',
}

def show_catalog(request):
    return render(request, "katalog.html", context)