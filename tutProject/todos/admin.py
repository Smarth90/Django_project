from django.contrib import admin

from .models import Person, Todo

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'todo_count')
    search_fields = ('name',)

    @admin.display(description='Todos')
    def todo_count(self, person):
        return person.todos.count()

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'priority', 'deadline', 'done')
    search_fields = ('title', 'description', 'owner__name')
    list_filter = ('done', 'priority', 'deadline')
    list_select_related = ('owner',)
