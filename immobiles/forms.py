from django import forms
from django.contrib.auth.models import User

from immobiles.models import Immobile


class ImmobileForm(forms.ModelForm):
    """ImmobileForm"""
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label='Responsável')

    class Meta:
        model = Immobile
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        inst = super().save(commit=False)
        inst.user = self.user
        if commit:
            inst.save()
            self.save_m2m()
        return inst
