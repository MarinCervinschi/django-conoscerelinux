from django.views.generic.detail import DetailView

from .models import StaticPage


class StaticPageView(DetailView):
    model = StaticPage
    template_name = "pages/static.html"
    context_object_name = "page"
