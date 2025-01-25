from django import forms

class Contact_form(forms.Form):

    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)