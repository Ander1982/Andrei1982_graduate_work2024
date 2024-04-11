from django import forms
from django.forms import ModelForm
from .models import Review


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    sms = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))


class RecordingForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    day = forms.DateField()
    time = forms.TimeField()


# class RecordingForm(ModelForm):
#     class Meta:
#         model = Recording
#         fields = ['staff', 'works', 'service', 'day']
#         widgets = {'staff': forms.CheckboxSelectMultiple()}
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         for field in self.fields.values():
#             field.widget.attrs.update({'class': 'input'})


# class RecordingForm(forms.Form):
#     name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
#     staff = forms.BooleanField()
#     works = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
#     service = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
#     day = forms.DateField()
#     time = forms.TimeField()


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Оставь отзыв',
            'body': 'Напиши комментарий на свой отзыв'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})
