from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core import serializers

from immobiles.forms import ImmobileForm
from immobiles.models import Immobile


class HomeView(TemplateView):
    template_name = 'immobiles/home.html'

    def get_context_data(self):
        context = super().get_context_data()
        immobiles = list()
        for immobile in Immobile.objects.filter(approved=True):
            immobiles.append(
                {
                    'id': immobile.id,
                    'user': immobile.user.get_full_name() or immobile.user.username,
                    'title': immobile.title,
                    'gender': immobile.get_gender_display(),
                    'kind': immobile.get_kind_display(),
                    'address': immobile.address,
                    'value': immobile.value,
                    'contact': immobile.contact,
                    'details': immobile.details,
                    'latitude': immobile.latitude,
                    'longitude': immobile.longitude,
                }
            )
        context['immobiles'] = immobiles
        return context


class CreateImmobile(LoginRequiredMixin, CreateView):
    template_name = 'immobiles/editor.html'
    form_class = ImmobileForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
