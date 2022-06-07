from django import forms
from home.models import CRUD

class CrudForm(forms.ModelForm):
    
    class Meta:
        model = CRUD
        fields = '__all__'