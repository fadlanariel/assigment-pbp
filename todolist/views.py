from django.shortcuts import render
from todolist.models import MyTodoList
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = MyTodoList.objects.all()
    context = {
        'data_todolist' : data_todolist,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def show_todolist_xml(request):
    data_todolist = MyTodoList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_todolist), content_type="application/xml")

# Forms
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    return render(request, 'create_task.html')

def addTaskView(request):
    taskname = request.POST['title']
    desc = request.POST['description']
    new_task = MyTodoList(user=request.user, title=taskname, description=desc, date=datetime.date.today())
    new_task.save()
    return HttpResponseRedirect('/todolist/')