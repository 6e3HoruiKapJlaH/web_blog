from django import forms

# Форма для оставления комментариев под статьями
class CommentForm(forms.Form):
    #Поля формы соответсятвуют models.Contacts
    nickname = forms.CharField( max_length=50)
    text = forms.CharField( max_length = 350, widget=forms.Textarea(attrs={ 'cols':30, 'rows':6}))
    avatar = forms.ImageField()