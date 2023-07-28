from django import forms
from .models import Viewing , Property


class ViewingForm(forms.ModelForm):
    class Meta :
        model = Viewing
        fields = '__all__'
