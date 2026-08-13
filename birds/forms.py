from django import forms
from .models import Bird, WeightRecord, BehaviorRecord

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
        fields = ['date', 'category', 'memo', 'photo']

        labels = {
            'date': '日付',
            'category': 'カテゴリ',
            'memo': 'メモ',
            'photo': '写真',
        }

        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

class BirdForm(forms.ModelForm):

    GENDER_CHOICES = [
        ('', '未登録'),
        ('オス', 'オス'),
        ('メス', 'メス'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=False,
        label='性別'
    )

    class Meta:
        model = Bird
        fields = ['name', 'color', 'gender', 'birthday', 'welcome_date', 'photo',]

        labels = {
            'name': '名前',
            'color': '種類',
            'birthday': '誕生日',
            'welcome_date': 'お迎え日',
            'photo': 'プロフィール写真',
        }

        widgets = {
            'birthday': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'welcome_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }