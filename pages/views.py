from django.contrib.auth.views import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
