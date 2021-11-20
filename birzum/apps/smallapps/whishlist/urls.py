from django.urls import path
from .views import whishlist_view


app_name = "whishlist"

urlpatterns = [
    path('', whishlist_view, name="whishlist")
]
