from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("nueva/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/editar/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/eliminar/", TaskDeleteView.as_view(), name="task-delete"),
]
