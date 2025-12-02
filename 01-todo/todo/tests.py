from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Todo

class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(title="Test Todo")
        self.assertEqual(todo.title, "Test Todo")
        self.assertFalse(todo.completed)
        self.assertIsNone(todo.due_date)

    def test_create_todo_with_due_date(self):
        due_date = timezone.now()
        todo = Todo.objects.create(title="Dated Todo", due_date=due_date)
        self.assertEqual(todo.due_date, due_date)

    def test_string_representation(self):
        todo = Todo.objects.create(title="My Todo")
        self.assertEqual(str(todo), "My Todo")

class TodoViewTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(title="Existing Todo")

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Existing Todo")
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_todo_create_view(self):
        response = self.client.post(reverse('todo-create'), {
            'title': 'New Todo',
            'completed': False
        })
        self.assertEqual(response.status_code, 302) # Redirects to list
        self.assertEqual(Todo.objects.count(), 2)
        self.assertTrue(Todo.objects.filter(title='New Todo').exists())

    def test_todo_update_view(self):
        response = self.client.post(reverse('todo-update', args=[self.todo.pk]), {
            'title': 'Updated Todo',
            'completed': True
        })
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Todo')
        self.assertTrue(self.todo.completed)

    def test_todo_delete_view(self):
        response = self.client.post(reverse('todo-delete', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)

    def test_todo_complete_view(self):
        response = self.client.post(reverse('todo-complete', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.completed)

