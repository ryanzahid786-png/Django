from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("todo/", views.todo, name="todo"),
    path("todo/<int:task_id>/complete/", views.complete_task, name="complete_task"),
    path("todo/<int:task_id>/delete/", views.delete_task, name="delete_task"),
]
