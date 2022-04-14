from django import forms
from .models import Vote, Comment

class VoteForm(forms.ModelForm):
    
    subject= forms.CharField(
        widget=forms.TextInput(
            attrs={
                    'class': 'form-control'
            }
        )
    )

    choice_one = forms.CharField(
        label='First Option',
        widget=forms.TextInput(
            attrs={
                    'class': 'form-control'
            }
        )
    )

    choice_two = forms.CharField(
        label='Second Option',
        widget=forms.TextInput(
            attrs={
                    'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Vote
        fields = ('subject', 'choice_one', 'choice_two')


class CommentForm(forms.ModelForm):

    choice = forms.CharField(
        label='Pick',
        widget = forms.Select(
            choices =[] ,
            attrs={
                'class':'form-control'
            }
        )
    )
    
    content = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control'
            }
            )
    )

    class Meta:
        model = Comment
        fields = ('choice', 'content')