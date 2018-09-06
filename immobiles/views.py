from django.http import HttpResponse

from django.views.generic import TemplateView, CreateView

from immobiles.forms import ImmobileForm


class HomeView(TemplateView):
    template_name = 'immobiles/home.html'


class CreateImmobile(CreateView):
    template_name = 'immobiles/editor.html'
    form_class = ImmobileForm
