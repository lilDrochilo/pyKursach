from .models import Client
from .django.forms import ModelForm

class ClientForm(ModelForm):
    class Meta:
        model = Client
        field = ['age','first_name','phone_number','Sketch','contacts','date']