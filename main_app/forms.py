'''
Created on Jul 31, 2014

@author: mdesbois
'''
from django import forms
from main_app.models import Contact


class ContactForm(forms.Form):
    senderName = forms.CharField(max_length=100)
    senderEmail = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget = forms.Textarea(attrs={'cols': 70}))
    cc_myself = forms.BooleanField(required=False)
    