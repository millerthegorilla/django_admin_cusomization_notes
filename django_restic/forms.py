from django import forms

class ResticForm(forms.Form):
    repo = forms.CharField('')
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
