from .models import *
from django.forms import ModelForm



class blogForm(ModelForm):
    class Meta:
        model=BlogModel
        fields = ['content']