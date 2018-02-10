from django import forms
from .models import Golfers


class GolfSelectForm(forms.ModelForm):

    class Meta:

        model = Golfers
        fields = ('golferName',)
