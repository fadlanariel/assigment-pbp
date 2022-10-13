from urllib import response
from django.shortcuts import render
from todolist.models import MyTodoList
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = MyTodoList.objects.filter(user=request.user)

    return render(request, "todolist.html",)

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    data_todolist = MyTodoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_todolist), content_type="application/json")

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
    created_date = str(datetime.date.today())
    new_task = MyTodoList(user=request.user, title=taskname, description=desc, date=created_date)
    new_task.save()
    return HttpResponseRedirect('/todolist/')

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.user.is_authenticated:
        data_todolist = MyTodoList.objects.all()
        response_data = {}

        if request.POST.get('action') == 'post':
            title = request.POST.get('title')
            description = request.POST.get('description')
            date =  str(datetime.date.today())

            response_data['title'] = title
            response_data['description'] = description
            response_data['date'] = date

            MyTodoList.objects.create(
                user = request.user,
                title = title,
                description = description,
                date = date,
                )
            return JsonResponse(response_data)

    else:
        return redirect('todolist:login')

def delete(request, id):
    if request.user.is_authenticated:
        task = MyTodoList.objects.get(id=id)
        task.delete()
        response_data = {}
        return HttpResponseRedirect('/todolist/')
    else:
        return redirect('todolist:login')