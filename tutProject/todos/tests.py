from django.test import TestCase
from django.urls import reverse

from .models import Person, Todo


class TodoViewsTests(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name='Avery', age=28)
        self.todo = Todo.objects.create(
            title='Write tests',
            description='Add coverage for the todo workflow.',
            owner=self.person,
        )

    def test_todos_page_loads(self):
        response = self.client.get(reverse('todos'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Write tests')
        self.assertContains(response, 'Owner: Avery')

    def test_creating_a_todo_assigns_its_owner(self):
        response = self.client.post(
            reverse('todos'),
            {
                'title': 'Review pull request',
                'description': 'Review the starter project.',
                'owner': self.person.id,
                'deadline': '',
                'priority': '',
            },
        )

        self.assertRedirects(response, reverse('todos'))
        self.assertEqual(Todo.objects.get(title='Review pull request').owner, self.person)

    def test_toggle_requires_post_and_updates_status(self):
        url = reverse('toggle', args=[self.todo.id])
        self.assertEqual(self.client.get(url).status_code, 405)

        response = self.client.post(url)
        self.assertRedirects(response, reverse('todos'))
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.done)

    def test_delete_requires_post_and_removes_todo(self):
        url = reverse('delete', args=[self.todo.id])
        self.assertEqual(self.client.get(url).status_code, 405)

        response = self.client.post(url)
        self.assertRedirects(response, reverse('todos'))
        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())

    def test_person_page_shows_assigned_todos(self):
        response = self.client.get(reverse('person_details', args=[self.person.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Avery')
        self.assertContains(response, 'Write tests')
