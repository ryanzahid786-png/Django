from django.shortcuts import get_object_or_404, redirect, render

from .models import Task


def home(request):
    """Home page."""
    return render(request, "home.html")


def about(request):
    """About page."""
    return render(request, "about.html")


def todo(request):
    """To-do list page: show all tasks and add a new one."""
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Task.objects.create(title=title)
        return redirect("todo")

    tasks = Task.objects.order_by("-created_at")
    return render(request, "todo.html", {"tasks": tasks})


def complete_task(request, task_id):
    """Toggle a task completed / not completed."""
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("todo")


def delete_task(request, task_id):
    """Delete a task."""
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("todo")
