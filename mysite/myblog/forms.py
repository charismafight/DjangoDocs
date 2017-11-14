from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


UploadFileForm


class NameForm(forms.Form):
    your_name = forms.CharField(label='your name', max_length=100)


NameForm
