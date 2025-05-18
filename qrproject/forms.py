from django import forms

class QRCodeForm(forms.Form):
    name=forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':"Enter the name"
        }))
    
    url=forms.URLField(
        max_length=200,
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placeholder':'Enter the URL'
        }))