from django.views.generic import TemplateView
from .models import Menu


class IndexPageView(TemplateView):
    model = Menu
    template_name = "menu/index.html"
