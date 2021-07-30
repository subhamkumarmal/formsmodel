from django import forms
from django.forms import ValidationError
from .models import Students

class FillDetails(forms.ModelForm):
    # name=forms.CharField(widget=forms.TextInput,max_length=30,min_length=5)
    # age=forms.IntegerField(widget=forms.NumberInput)
    # email=forms.EmailField(widget=forms.EmailInput)
    # password=forms.CharField(widget=forms.PasswordInput)
    #
    # def clean(self):
    #     user_cleaned_data=super().clean();
    #     agev=user_cleaned_data['age']
    #     if int(agev)<18:
    #         raise ValidationError("enter the age above 18")
    students_age=forms.IntegerField(widget=forms.NumberInput)
    class Meta:
        model=Students
        labels={'students_name':'name','students_age':'age','students_email':'email','students_password':'password'}
        # fields:['students_name','students_age','students_email','students_password']
        exclude=['students_id']
        widgets={'students_name':forms.TextInput(attrs={'max_length':30,'min_length':5}),
                 'students_password':forms.PasswordInput()

                 }

    def clean(self):
        user_cleaned_data = super().clean();
        agev = user_cleaned_data['students_age']
        if int(agev) < 18:
            raise ValidationError("enter the age above 18")


class Log(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)

