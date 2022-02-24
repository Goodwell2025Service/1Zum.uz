from allauth.account.views import SignupView, LoginView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView
from django.shortcuts import render
from .models import Profile
from .forms import UserAddressCreationForm, BaseUserSignupForm #, BaseUserLoginForm
# from .forms import UserAddressCreationForm

User = get_user_model()

class UserAccountDashboardView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/account_dashboard.html"

user_account_dashboard_view = UserAccountDashboardView.as_view()

class UserAccountDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/account_details.html"

user_account_detail_view = UserAccountDetailView.as_view()

class UserAccountAddressesView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/account_addresses.html"


user_account_addresses_view = UserAccountAddressesView.as_view()

class UserAddressCreateView(CreateView):
    model = Profile
    form_class = UserAddressCreationForm
    template_name = "users/user_address_create_form.html"

    def form_valid(self, form):
        obj = form.save()
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]

user_address_create_view = UserAddressCreateView.as_view()

class UserAddressUpdateView(UpdateView):
    model = Profile
    form_class = UserAddressCreationForm
    template_name = "users/user_address_create_form.html"

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]


user_address_update_view = UserAddressUpdateView.as_view()


class UserAccountOrdersView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/account_orders.html"

user_account_orders_view = UserAccountOrdersView.as_view()

class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
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



class UserSignupView(SignupView):
    form_class = BaseUserSignupForm

    def get_success_url(self):
        return reverse("home")

    def form_invalid(self, form):
        return super().form_invalid(form)


user_signup_view = UserSignupView.as_view()

# class UserLoginView(LoginView):
#     model = User
#     form_class = BaseUserLoginForm

#     # def get_success_url(self):
#     #     return reverse("users:detail")

#     # def form_invalid(self, form):
#     #     return super().form_invalid(form)


# user_login_view = UserLoginView.as_view()
