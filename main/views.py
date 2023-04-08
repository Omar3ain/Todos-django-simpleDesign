from django.shortcuts import render, redirect

from main.forms import TodoForm, TodoItemsForm

from main.models import Todo, TodoItems
# Create your views here.

def home(request):
    context = {
            "todos": ""
        }
    try : 
        todos = Todo.objects.all()
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
