from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TodoForm, personForms
from .models import Person, Todo


# Create your views here.
def hello_world_view(request):
    return HttpResponse("Hello World")
def hello_python_view(request):
    return HttpResponse("Hello Python")
def render_hello_world(request):
    return render(request, 'todos/hello.html')
def hello_path(request, num1, num2):
    return HttpResponse(f"Sum is {num1 + num2}!") 
def hello_query(request):
    return HttpResponse(f"Your query was {request.GET.get('q')}")
def special_view(request):
    return redirect('render_hello_world')
def post_example(request):
    if request.method == 'POST':
        form = personForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            job = form.cleaned_data['job']
            return HttpResponse(f"You posted: {name}, {age}, {job}")
    else:
        return HttpResponseNotAllowed(['POST'])

def submit_example(request):
    return render(request, 'todos/submit.html')

def submit_django_form(request):
    form = personForms()
    return render(request, 'todos/submit_django_form.html', {'form': form})

def template_ex(request):
    context = {
        'name' : "Mike",
        "age" : 30,
        "skills" : ["Python", "Java", "Django"]
    }

    return render(request, "todos/template_example.html",context)

def Todos_view(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo added successfully.")
            return redirect('todos')

    todos = Todo.objects.select_related('owner').order_by('done', 'deadline', '-id')
    return render(request, 'todos/todos.html', {'todos': todos, 'form': form})
    
def person_details(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    todos = person.todos.order_by('done', 'deadline', '-id')
    return render(request, 'todos/person_details.html', {'person': person, 'todos': todos})

@require_POST
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    messages.success(request, "Todo deleted.")
    return redirect('todos')

@require_POST
def toggle_todo_done(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.done = not todo.done
    todo.save(update_fields=['done'])
    messages.success(request, "Todo status updated.")
    return redirect('todos')
