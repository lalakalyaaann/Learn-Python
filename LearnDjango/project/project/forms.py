from django import forms


class UserForm(forms.Form):
    num1 = forms.CharField(label="Marks 1", widget=forms.TextInput(attrs={'class': 'form-control'}))
    num2 = forms.CharField(label="Marks 2", widget=forms.TextInput(attrs={'class': 'form-control'}))