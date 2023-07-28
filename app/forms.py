from django import forms
from . models import Viewing


class ViewingForm(form.ModelForm):
    class Meta :
        models = Viewing
        fields = '__all__'
