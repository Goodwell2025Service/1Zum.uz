from django.views.generic import TemplateView


class CompareBox(TemplateView):
    template_name = "smallapps/compare/compare.html"


compare_view = CompareBox.as_view()
