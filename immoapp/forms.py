from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from immoapp.models import Immobilier, ImmageDB, Client, ClientAlert
from django.core.exceptions import ValidationError

class AddimageForm(forms.ModelForm):
    class Meta:
        model = ImmageDB
        fields = ('element', 'img')

class ClientForm(forms.ModelForm):
    def clean_cellphone_number(self):
        data = self.cleaned_data['cellphone_number']

        # Vérifier que la date ne se situe pas dans le passé.
        if len(data) != 8:
            raise ValidationError(('Invalid numero - renewal in past'), code='invalid')
        # N'oubliez pas de toujours renvoyer les données nettoyées.
        return data

    class Meta:
        model = Client
        fields = ('fullname', 'cellphone_number')
        #labels = {'cellphone_number': _('numero whatsapp svp')}
        #help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).')}

class AlertForm(forms.ModelForm):
    def clean_alertcontact(self):
        data = self.cleaned_data['alertcontact']

        # Vérifier que la date ne se situe pas dans le passé.
        if type(data) == int and len(str(data)) != 8:
            raise ValidationError(('Invalid numero - renewal in past'), code='invalid')
        # N'oubliez pas de toujours renvoyer les données nettoyées.
        return data

    class Meta:
        model = ClientAlert
        fields = ('created', 'alertname', 'lieux', 'typebien', 'typetransaction', 'budget', 'typecontact', 'alertcontact', 'commentaire' )