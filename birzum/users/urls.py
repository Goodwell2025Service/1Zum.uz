from django.urls import path

from birzum.users.views import * # user_detail_view, user_redirect_view, user_update_view

# django_view_set

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_account_dashboard_view, name="detail"),
    path("<str:username>/account_details/", view=user_update_view, name="account_details"),
    path("<str:username>/account_orders/", view=user_account_orders_view, name="account_orders"),
    path("<str:username>/account_addresses/", view = user_account_addresses_view, name="account_addresses"),
]
