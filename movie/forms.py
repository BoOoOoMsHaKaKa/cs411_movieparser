from django import forms
from .models import Movies,People
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields ="__all__"

class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields ="__all__"
