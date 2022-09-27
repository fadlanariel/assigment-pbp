from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, addTaskView, show_todolist_xml

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('addTask/', addTaskView),
    path('xml/', show_todolist_xml, name='show_todolist_xml'),
]