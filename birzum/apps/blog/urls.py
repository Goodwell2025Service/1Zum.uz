from django.urls import path

from .views import list_view, detail_view

app_name = "blog"

urlpatterns = [
    path("", list_view, name="list"),
    path("detail/", detail_view, name="detail")
]

