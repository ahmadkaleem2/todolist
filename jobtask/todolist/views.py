from typing import List
from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponse
from django.urls import reverse
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import (CreateView,ListView,UpdateView,DeleteView)

from .models import TodoList
from .forms import TodoForm

def defaultview(request):
    return HttpResponse("hey")



class TodoCreate(CreateView):
    template_name = 'todolist/TodoList_create.html'
    form_class = TodoForm
    queryset = TodoList.objects.all()

    def get_success_url(self):
        return reverse('todolist:list')
class TodoList1(ListView):
    template_name = 'todolist/TodoList_List.html'
    queryset = TodoList.objects.all()


class TodoDelete(DeleteView):
    template_name = 'todolist/TodoList_delete.html'
    
    success_url = reverse_lazy("todolist:list")

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(TodoList,id=id_)
        
class TodoUpdate(UpdateView):
    template_name = 'todolist/TodoList_create.html'
    form_class = TodoForm
    queryset = TodoList.objects.all()
    success_url = reverse_lazy('todolist:list')
    def get_object(self):
        id_ = self.kwargs.get("pk")
        
        return get_object_or_404(TodoList,id=id_)
    
    
    

    
    