from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from .forms import personForms


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