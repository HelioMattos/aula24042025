from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from .models import Todo
from django.shortcuts import get_object_or_404, redirect
from datetime import date


# Create your views here.

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')
    
class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished_at = date.today()
        todo.save()
        return redirect("todo_list")
