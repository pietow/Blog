from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField(required=False)
    body = forms.CharField(label='Kommentar', widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
