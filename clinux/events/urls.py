from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.EventSessionListView.as_view(), name="events"),
    path("list", views.EventListView.as_view(), name="event-list"),
]
