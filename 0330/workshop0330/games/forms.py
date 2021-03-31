from django import forms
from .models import Game, Comment


class GameForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 5,
                'cols': 20,
            }
        )
    )
    left_side = forms.CharField(
        label = '선택1',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
               
            }
        )
    )
    right_side = forms.CharField(
        label = '선택2',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                
                
            }
        )
    )


    class Meta:
        model = Game
        fields = '__all__'
        exclude = ('user','left_number','right_number')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('game', 'user',)
        




