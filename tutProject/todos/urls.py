from django.urls import path
from . import views



urlpatterns = [
    path('hello', views.hello_world_view, name = 'hello_world_view' ),
    path('hellopy', views.hello_python_view, name = 'hello_python_view'),
    path('', views.render_hello_world, name = 'render_hello_world'),
    path('helloquery', views.hello_query, name = 'helloQuery'),
    path('postendpoint', views.post_example, name = 'postend'),
    path('submitForm', views.submit_example, name = 'submitForm'),
    path('add/<int:num1>/<int:num2>', views.hello_path, name = 'add'),
    path('redirectthis', views.special_view, name='redirectthis')
]
