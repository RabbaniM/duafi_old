# -*- coding: utf-8 -*-
from django import forms



#Start contact ========================================================================


class ContactForm(forms.Form):

    name = forms.CharField()
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)

#End contact ========================================================================

