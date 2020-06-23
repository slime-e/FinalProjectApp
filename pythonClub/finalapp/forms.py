from django import forms
from .models import Dog, Breed, DogReview


class DogForm(forms.ModelForm):
    class Meta:
        model=Dog
        fields='__all__'


class BreedForm(forms.ModelForm):
    class Meta:
        model=Breed
        fields='__all__'