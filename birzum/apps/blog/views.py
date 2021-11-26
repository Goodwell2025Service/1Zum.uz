from django.views.generic import TemplateView


# Create your views here.
class BlogListView(TemplateView):
    template_name = "blog/blog_list.html"


list_view = BlogListView.as_view()


class BlogDetailView(TemplateView):
    template_name = "blog/blog_detail.html"


detail_view = BlogDetailView.as_view()
