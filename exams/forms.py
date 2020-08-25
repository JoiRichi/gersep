from django import forms

from django.forms.utils import ValidationError

from .models import Submission


class ExamForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = {

            'email',
            'question',
            'candidate_code',
            'text',

        }

        widgets = {

            'candidate_code': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'required': 'required'}),


        }

class GetUsers(forms.Form):
    email= forms.CharField(max_length= 250,label="Enter email")
