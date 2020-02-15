from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botchat = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    #requied = false for hidden field
    # def clean_botchat(self):
    #     botchat = self.cleaned_data['botchat']
    #     if len(botchat) > 0:
    #         raise forms.ValidationError("GOTACHA BOT")
    #     return botchat
