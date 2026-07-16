from django import forms
from .models import WeightRecord, BehaviorRecord

class WeightRecordForm(forms.ModelForm):
    class Meta:
        model = WeightRecord
        fields = ['date', 'weight', 'memo']

class BehaviorRecordForm(forms.ModelForm):
    class Meta:
        model = BehaviorRecord
        fields = ['date', 'category', 'memo']
