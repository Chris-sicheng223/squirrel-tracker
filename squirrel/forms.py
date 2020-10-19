from django.forms import ModelForm, DateInput, DateField

from .models import Sighting

class SightingRequestForm(ModelForm):
    date=DateField(input_formats=['%m%d%Y'], help_text='Format:mmddyyyy')
    class Meta:
        model = Sighting
        fields = '__all__'

class SightingUpdateForm(ModelForm):
    date = DateField(input_formats=["%m%d%Y"], widget=DateInput(format='%m%d%Y'), help_text='Format:mmddyyyy')
    class Meta:
        model = Sighting
        fields = [
                'latitude', 
                'longitude', 
                'unique_squirrel_id', 
                'shift', 
                'date', 
                'age',
        ]
