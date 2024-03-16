from django import forms

GENDER_CHOICE = (
    ("M", "Male"),
    ("F", "Female"),
    ("0", "Not stated")
)

class GenderForm(forms.Form):
    gender_field = forms.ChoiceField(choices=GENDER_CHOICE)