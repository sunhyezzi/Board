from django import forms
from.models import Board,Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board #Myapp과 연결
        fields = ['title','body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = '댓글'