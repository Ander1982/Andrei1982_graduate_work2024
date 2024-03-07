from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    sms = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))


class RecordForm(forms.Form):
    data = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': "form-control"}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': "form-control"}))