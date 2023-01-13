from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        exclude = ('user', )



class CommentForm(forms.ModelForm):
    
        
    class Meta:
        model = Comment
        # fields = ('content', )
        exclude = ('article', 'user',)

    
    # class Meta:
    #     # model = Comment
    #     # fields = '__all__' 을 하면 fields에 있는 content와 article 이 다 들어와서 
    #     # fields = ('content', ) 하거나 
    #     # exclude = ('article', ) 해야 한다.
 
    #     # fields = ('content', )
    #     exclude = ('article', 'user', )
 