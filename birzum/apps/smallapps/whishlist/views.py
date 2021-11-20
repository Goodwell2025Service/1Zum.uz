from django.views.generic import TemplateView


class Whishlist(TemplateView):
    template_name = "smallapps/whishlist/whishlist.html"


whishlist_view = Whishlist.as_view()
