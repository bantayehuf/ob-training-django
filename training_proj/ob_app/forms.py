from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(label="Title")
    page = forms.IntegerField(label='Pages')
