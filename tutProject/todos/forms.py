from django import forms

from .models import Todo


class personForms(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    age = forms.IntegerField(label="Your Age")
    job = forms.CharField(max_length=100, required=False, label="Your Job")


class Todo_form(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "done", "deadline", "priority"]
        widgets = {"deadline": forms.DateInput(attrs={"type": "date"})}
