from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
    ordering = ['-created_at']

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'due_date', 'completed']
    success_url = reverse_lazy('todo-list')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'due_date', 'completed']
    success_url = reverse_lazy('todo-list')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo-list')

class TodoCompleteView(UpdateView):
    model = Todo
    fields = []
    success_url = reverse_lazy('todo-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.completed = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
