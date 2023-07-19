from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.Root.as_view(), name="root"),
]
