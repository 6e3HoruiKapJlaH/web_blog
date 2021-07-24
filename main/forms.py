from django import forms

class CommentForm(forms.Form):
    nickname = forms.CharField(label='Enter username:', max_length=50)
    text = forms.CharField(label='Leave a comment:', max_length = 350, widget=forms.Textarea(attrs={ 'cols':30, 'rows':6}))
    avatar = forms.ImageField(label='Leave a comment:')