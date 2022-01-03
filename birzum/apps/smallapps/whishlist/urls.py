from django.urls import path

from . import views

app_name = 'whishlist'

urlpatterns = [
    path('', views.whishlist_detail, name='whishlist'),
    path('add/<int:id>/', views.whishlist_add, name='add'),
    path('remove/<int:product_id>/', views.whishlist_remove, name='remove'),
    path('clear/', views.whishlist_clear, name='clear'),
]
