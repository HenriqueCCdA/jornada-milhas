from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("depoimentos/<int:pk>/", views.rud_post, name="post-retrieve-update-destroy"),
    path("depoimentos/", views.lc_post, name="post-list-create"),
    path("depoimentos-home/", views.post_home, name="post-home"),
    #
    path("destinos/<int:pk>/", views.rud_destination, name="destination-retrieve-update-destroy"),
    path("destinos/", views.lc_destination, name="destination-list-create"),
]
