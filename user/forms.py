from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User # model that will be affected
        # now has additional email form
        fields = ['username','email','password1','password2'] # what we want in the form and in which order

#class UserPreferenceForm
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User # model that will be affected
        # now has additional email form
        fields = ['username','email'] # what we want in the form and in which order

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile # model that will be affected
        # now has additional email form
        fields = ['favorite_movies','favorite_actors','favorite_directors','image'] # what we want in the form and in which order
