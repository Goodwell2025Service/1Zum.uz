from django.views.generic import ListView, DetailView

from .models import New

# Create your views here.
class BlogListView(ListView):
    model = New

    def get_queryset(self):
        qs =  super().get_queryset()
        q = self.request.GET.get('q', None)
        discount = self.request.GET.get('discount', None)
        new = self.request.GET.get('new', None)
        if q:
            qs = qs.filter(title__icontains=q)
        if discount:
            qs = qs.filter(stock=True)
        if new:
            qs = qs.filter(news=True)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news"] = New.objects.all().order_by('-created')[:6]
        return context
    


list_view = BlogListView.as_view()


class BlogDetailView(DetailView):
    model = New
    slug_field = "slug"


detail_view = BlogDetailView.as_view()
