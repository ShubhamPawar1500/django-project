from django import forms
from .models import customer, fooditem, reviews
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class create_customer(forms.ModelForm):
     class Meta:
          model = customer
          fields = '__all__'

class create_food(forms.ModelForm):
     class Meta:
          model = fooditem
          fields = '__all__'

class create_review(forms.ModelForm):
     class Meta:
          model = reviews
          fields = '__all__'
     
class Userform(UserCreationForm):
     email = forms.EmailField(required=True)
     class Meta:
          model = User
          fields = ('username','email', 'password1','password2')