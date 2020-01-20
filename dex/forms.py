from django import forms

from .models import Detail

class DetailForm(forms.ModelForm):

    class Meta:
        model = Detail
        fields = ('title', 'text',)