from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

app_name = "rating"

urlpatterns = [
    path('rate/<int:id>/', views.rate, name='rate')
]
