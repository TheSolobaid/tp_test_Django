from django.forms import ModelForm, ChoiceField, ValidationError
from django.utils.translation import gettext_lazy as _
from . import models

class Auto_Form(ModelForm):
    class Meta:
        model = models.auto
        fields = ('model','marque','date_achat','nombre_place','description','longeur','clim')
        labels = {
            'model' : _('Model'),
            'marque' : _('Marque'),
            'date_achat' : _('Date d’achat'),
            'nombre_place' : _('Nombre de places'),
            'description' : _('Description'),
            'longeur' : _('longueur du véhicule'),
            'clim' : _('La voiture possède-t-elle la climatisation?'),
        }