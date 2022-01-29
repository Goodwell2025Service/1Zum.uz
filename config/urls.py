from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from birzum.homeviews import HomeView


def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = (
    i18n_patterns(
        path("", HomeView.as_view(), name="home"),
        path("coming-soon/", TemplateView.as_view(template_name="pages/soon.html"), name="soon"),
        # Django Admin, use {% url 'admin:index' %}
        path(settings.ADMIN_URL, admin.site.urls),
        path("translations/", include("rosetta.urls")),
        # path("hijack", include('hijack.urls', namespace='hijack')),
        # User management
        path("users/", include("birzum.users.urls", namespace="users")),
        path("accounts/", include("allauth.urls")),
        path('ckeditor/', include('ckeditor_uploader.urls')),
        # Your stuff: custom urls includes go here
        path("cart/", include('birzum.apps.cart.urls', namespace='cart')),
        path("blog/", include('birzum.apps.blog.urls', namespace='blog')),
        path("whishlist/", include('birzum.apps.smallapps.whishlist.urls', namespace='whishlist')),
        path("compare/", include('birzum.apps.smallapps.compare.urls', namespace='compare')),
        path("company/", include('birzum.apps.smallapps.company.urls', namespace='company')),
        path("order/", include('birzum.apps.order.urls', namespace='order')),
        path("rate/", include('birzum.apps.smallapps.rating.urls', namespace='rating')),
        path("", include('birzum.apps.products.urls', namespace="products")),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
