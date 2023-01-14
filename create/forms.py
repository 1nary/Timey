from django import forms
from create.models import Lecture

class createForm(forms.ModelForm):
  class Meta:
    model = Lecture
    fields = ['name','teacher','room','week','period']
    widgets = {
      'name': forms.TextInput(attrs= {
        'placeholder': '講義を入力してください',
        'class': 'form__input form__input-type--text',
      }),
      'teacher':forms.TextInput(attrs= {
        'placeholder': '担当教員を入力してください',
        'class': 'form__input form__input-type--text',
      }),
      'room': forms.TextInput(attrs= {
        'placeholder': '教室を入力してください',
        'class': 'form__input form__input-type--text',
      }),
      'week': forms.RadioSelect(attrs={'class': 'form__input form__input-type--radio'}),
      'period': forms.RadioSelect(attrs={'class': 'form__input form__input-type--radio'})
    }