from django.views.generic import ListView, DetailView

from .models import New

# Create your views here.
class BlogListView(ListView):
    model = New


list_view = BlogListView.as_view()


class BlogDetailView(DetailView):
    model = New
    slug_field = "slug"


detail_view = BlogDetailView.as_view()
