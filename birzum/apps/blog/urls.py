from django.urls import path

from .views import detail_view, list_view

app_name = "blog"

urlpatterns = [
    path("", list_view, name="list"),
    path("<slug:slug>/", detail_view, name="detail")
]
