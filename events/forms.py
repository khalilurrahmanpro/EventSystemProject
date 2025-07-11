from django import forms
from .models import Event
from .models import Category
from .models import Participant

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'