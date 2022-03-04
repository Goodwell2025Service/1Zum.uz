from django.urls import path

from birzum.users.views import user_address_update_view, user_address_create_view,user_redirect_view, user_update_view, user_account_dashboard_view, user_account_addresses_view, user_account_orders_view, user_account_detail_view

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/detail/", view=user_account_dashboard_view, name="detail"),

    path("<str:username>/account_details/", view = user_account_detail_view, name="account_details"),
    path("<str:username>/account_details_update/", view=user_update_view, name="account_details_update"),

    path("<str:username>/account_orders/", view=user_account_orders_view, name="account_orders"),

    path("<str:username>/account_addresses/", view = user_account_addresses_view, name="account_addresses"),
    path("account_addresses/create/", view = user_address_create_view, name="address_create"),
    path("<str:username>/address/<int:pk>/change/", view = user_address_update_view, name="address_change"),
]
