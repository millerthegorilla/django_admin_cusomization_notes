from django import forms

class Restic(forms.Form):
    # repo = forms.CharField('')
    # snapshots = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=(),
    # )
    def __init__(self, repos: list) -> None:
        super().__init__()
        for i, path in enumerate(repos.keys()):
            choices = ()
            for j, snapshot in repos[path]:
                choices = (j, snapshot)
            breakpoint()
            self.fields[path] = forms.CharField(label='Repo {}'.format(str(i)), initial=path, disabled=True)
            self.fields[path + "_snapshots"] = forms.MultipleChoiceField(label='', required=False,
                                                                widget=forms.CheckboxSelectMultiple,
                                                                choices=choices)
