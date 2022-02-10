from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView
from django.shortcuts import render
from .forms import *
from django.shortcuts import get_object_or_404

User = get_user_model()

#  account_dashboard_view

class UserAccountDashboardView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/account_dashboard.html"


user_account_dashboard_view = UserAccountDashboardView.as_view()

# account_details_view

class UserAccountDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/account_details.html"


user_account_detail_view = UserAccountDetailView.as_view()

# account_addresses_view

class UserAccountAddressesView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/account_addresses.html"


user_account_addresses_view = UserAccountAddressesView.as_view()

# account_orders_view

class UserAccountOrdersView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/account_orders.html"


user_account_orders_view = UserAccountOrdersView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    # form_class = UserChangeForm
    # get_initial - UpdateView
    fields = ['first_name', 'last_name','username', 'email',]
    template_name = "users/account_details.html"

    success_message = _("Information successfully updated")

    def form_valid(self, form):
        return super().form_valid(form)



    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]
    

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
