from django.forms import ModelForm
from .models import Livre


class LivreForm(ModelForm):

    class Meta:

        model = Livre

        fields = (
            'titre',
            'auteur',
            'date_parution',
            'nombre_pages',
            'resume'
        )