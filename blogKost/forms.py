# -*- coding: utf-8 -*- 

from django import forms


# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Ваше имя:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Что Вас интересует?"