from django.urls import path

from .views import order_create_view, order_succeeded_view

app_name = "order"

urlpatterns = [
    path("", order_create_view, name="create"),
    path("sent/", order_succeeded_view, name="success")
]
