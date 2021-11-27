from django.views.generic import DetailView


from .models import AboutUs, Leaders, Awards

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
