from django.views.generic import ListView, DetailView

from .models import New

# Create your views here.
class BlogListView(ListView):
    model = New

    def get_queryset(self):
        qs =  super().get_queryset()
        q = self.request.GET.get('q', None)
        if q:
            return qs.filter(title__icontains=q)
        return qs


list_view = BlogListView.as_view()


class BlogDetailView(DetailView):
    model = New
    slug_field = "slug"


detail_view = BlogDetailView.as_view()
