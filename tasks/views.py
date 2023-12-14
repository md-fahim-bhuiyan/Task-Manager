
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from .models import Task
from .forms import TaskForm

from django.db.models import Q

class TaskListView(View):
    template_name = 'tasks/task_list.html'

    def get(self, request):
        query = request.GET.get('q', '')

        if query:
            tasks = Task.objects.filter(Q(title__icontains=query))
        else:
            tasks = Task.objects.all()

        return render(request, self.template_name, {'tasks': tasks, 'query': query})


class TaskCreateView(View):
    template_name = 'tasks/task_create.html'

    def get(self, request):
        form = TaskForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('task_list'))
        return render(request, self.template_name, {'form': form})

class TaskDetailView(View):
    template_name = 'tasks/task_detail.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, self.template_name, {'task': task})

class TaskUpdateView(View):
    template_name = 'tasks/task_update.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, self.template_name, {'form': form, 'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse('task_detail', args=[pk]))
        return render(request, self.template_name, {'form': form, 'task': task})

class TaskDeleteView(View):
    template_name = 'tasks/task_delete.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, self.template_name, {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect(reverse('task_list'))
