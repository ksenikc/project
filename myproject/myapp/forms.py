from .models import Application
from django.forms import ModelForm, TextInput, Textarea, forms


class NewApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['title', 'description', 'categor', 'photo']
        widgets = {
            "date": TextInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

        }

class UpdateForm(ModelForm):
   model = Application
   fields = ['stat', 'image_after']


class UpdatesForm(ModelForm):
   model = Application
   fields = ['stat', 'rejection_reason']
