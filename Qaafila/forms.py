from django import forms
from .models import Darja, Comment

class DarjaForm(forms.ModelForm):
  class Meta:
    model = Darja
    fields = ['text']
    labels = {'text':''}
    widgets = {
      'text' : forms.Textarea(
        attrs={'placeholder':'Enter your Text',
               'rows':3
               }
               )
    }


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']
    widgets = {
      'comment': forms.Textarea(attrs={
        'placeholder':'Write your comment',
        'rows':2
      })
    }
    labels = {'comment':''}