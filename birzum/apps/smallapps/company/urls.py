from django.urls import path

from .views import about_view, contact_view


app_name = "company"

urlpatterns = [
    path("", about_view, name="about"),
    path("contact/", contact_view, name="contact"),
]

