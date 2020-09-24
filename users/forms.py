from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','age','email', )

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields