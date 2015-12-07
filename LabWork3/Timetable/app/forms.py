from django import forms


class TimetableSearchForm(forms.Form):
    group = forms.IntegerField()
