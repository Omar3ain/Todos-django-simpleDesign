from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, TodoItems
from .forms import TodoForm, userCreation

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .filters import TodoFilter
# Create your views here.

@login_required(login_url = 'login')
def home(request):
    context = {
            "todos": ""
        }
    try : 
        user = request.user
        todos = Todo.objects.filter(user=user)
    except:
        return render(request,'components/home.html' , context)
    context = {
            "todos": todos
        }
    return render(request,'components/home.html', context)


def details(request,id):
    todo = Todo.objects.get(id = id)
    items = todo.todoitems_set.all()
    context = {
        'items': items
    }
    return render(request,'components/details.html',context)

def createTodo(request):
    form = TodoForm()
    if request.method == 'POST':
        form =  TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form,
    }
    return render(request, 'components/createTodo.html',context)
def createTodoItem(request):
    form = TodoItemsForm()
    if request.method == 'POST':
        form =  TodoItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "itemform": form,
    }
    return render(request, 'components/createItemTodo.html',context)

def updateTodoItem(request, pk):
    todoItem = TodoItems.objects.get(id=pk)
    form= TodoItemsForm(instance=todoItem)
    if request.method == 'POST':
        form = TodoItemsForm(request.POST, instance=todoItem)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'components/updateItem.html', context)

def deleteTodoItem(request, pk):
    todoItem = TodoItems.objects.get(id=pk)
    todoItem.delete()
    return redirect('/')

def createUser(request):
    form = userCreation()
    if request.method == 'POST':
        form = userCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    context = {
        'form': form
    }
    return render(request, 'components/signup.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request , user)
            return redirect('/')
    context = {}
    return render(request, 'components/login.html', context)

def createUser(request):
    form = UserCreation()
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form,
    }
    return render(request, 'signup.html', context)

def logoutUser(request):
    user = request.user
    logout(request) 
    return redirect('/login')