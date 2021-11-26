from django.urls import path

from .views import compare_view

app_name = "compare"

urlpatterns = [
    path('', compare_view, name="compare")
]
