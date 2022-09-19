from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
data_mywatchlist = MyWatchList.objects.all()
context = {
    'watchlist': data_mywatchlist,
    'nama': 'Fadlan Ariel Fathurrahman',
    'npm' : '2106750673',
}

def show_watchlist(request):
    return render(request, "mywatchlist.html", context)

def show_watchlist_xml(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_watchlist_json(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")