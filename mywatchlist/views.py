from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
data_mywatchlist = MyWatchList.objects.all()
mywatchlist_list = list(data_mywatchlist)
watchcount = 0

for film in mywatchlist_list:
    if film.watched == True:
        watchcount += 1

if watchcount >= len(mywatchlist_list)/2:
    msg = "Selamat, kamu sudah banyak menonton!"
else:
    msg = "Wah, kamu masih sedikit menonton!"
context = {
    'watchlist': data_mywatchlist,
    'nama': 'Fadlan Ariel Fathurrahman',
    'npm' : '2106750673',
    'message' : msg,
}

def show_watchlist(request):
    return render(request, "mywatchlist.html", context)

def show_watchlist_xml(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_watchlist_json(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")