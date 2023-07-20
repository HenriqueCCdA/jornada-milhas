from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("depoimentos/<int:pk>/", views.rud_post, name="post-retrieve-update-destroy"),
    path("depoimentos/", views.lc_post, name="post-list-create"),
]
