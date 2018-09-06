from django import forms

from immobiles.models import Immobile


class ImmobileForm(forms.ModelForm):
    """ImmobileForm"""

    class Meta:
        model = Immobile
        fields = '__all__'
