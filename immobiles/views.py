from django.http import HttpResponse
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core import serializers

from immobiles.forms import ImmobileForm
from immobiles.models import Immobile, GENDERS, KINDS


class HomeView(TemplateView):
    http_method_names = ['get', 'post']
    template_name = 'immobiles/home.html'

    def get_context_data(self):
        context = super().get_context_data()
        immobiles = list()
        for immobile in self.get_queryset():
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
        context['genders'] = GENDERS
        context['kinds'] = KINDS
        context['selected_genders'] = self.request.POST.getlist('genders', [])
        context['selected_kinds'] = self.request.POST.getlist('kinds', [])
        context['initial_value'] = self.request.POST.get('initial_value', 0)
        context['final_value'] = self.request.POST.get('final_value', 5000)
        return context

    def get_queryset(self):
        object_list = Immobile.objects.filter(approved=True)
        initial_value = self.request.POST.get('initial-value', False)
        final_value = self.request.POST.get('final-value', False)
        genders = self.request.POST.getlist('genders', False)
        kinds = self.request.POST.getlist('kinds', False)

        if initial_value:
            object_list = object_list.filter(value__gte=initial_value)
        if final_value:
            object_list = object_list.filter(value__lte=final_value)
        if genders:
            object_list = object_list.filter(gender__in=genders)
        if kinds:
            object_list = object_list.filter(kind__in=kinds)
        return object_list

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class CreateImmobile(LoginRequiredMixin, CreateView):
    template_name = 'immobiles/editor.html'
    form_class = ImmobileForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
