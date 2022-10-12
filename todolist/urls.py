from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, addTaskView, show_todolist_json, add_task, delete

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('addTask/', addTaskView),
    path('json/', show_todolist_json, name='json'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:id>', delete, name='delete'),
]