from django.urls import path

from .views import home_view, product_detail_view, product_list_view

app_name = "products"

urlpatterns = [
    path('', home_view, name="home"),
    path('list/', product_list_view, name="list"),
    path('list/<slug:cat_slug>/', product_list_view, name="list_by_category"),
    path('<slug:cat_slug>/<slug:slug>/', product_detail_view, name="detail")
]
