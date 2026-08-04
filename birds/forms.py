from django import forms
from .models import WeightRecord, BehaviorRecord

class WeightRecordForm(forms.ModelForm):
    class Meta:
        model = WeightRecord
        fields = ['date', 'weight', 'memo']
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

class BehaviorRecordForm(forms.ModelForm):
    class Meta:
        model = BehaviorRecord
        fields = ['date', 'category', 'memo']
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }