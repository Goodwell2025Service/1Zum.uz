from django.views.generic import DetailView, CreateView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse 

from birzum.apps.blog.models import Savollar
from .models import AboutUs, Leaders, Awards, Contact, Message
from .forms import MessageForm


class About(DetailView):
    model = AboutUs
    template_name = "pages/about.html"

    def get_queryset(self):
        return super().get_queryset()
    
    def get_object(self):
        qs = self.get_queryset()
        return qs.first()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["leaders"] = Leaders.objects.all()
        context["awards"] = Awards.objects.all()
        return context
    
    
about_view = About.as_view()


class ContactUs(CreateView):
    model = Message
    template_name = "pages/contact.html"
    form_class = MessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions"] = Savollar.objects.all()
        context["contact"] = Contact.objects.first()
        return context

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _("Sizning xabaringiz yuborildi"))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.WARNING, _("Quyidagi xatolarni to'g'irlang!"))
        return super().form_invalid(form)

    def get_succes_url(self):
        return reverse('company:contact')


contact_view = ContactUs.as_view()
