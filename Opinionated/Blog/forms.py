
from Blog.models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    
    class Meta:
        model=Post
        fields=('author','title','text')
        widgets={ #set up classes to edit widget css
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}) 
        }


class CommentForm(forms.ModelForm):
    
    class Meta:
        model=Comment
        fields=('author','text')

        widgets={ #set up classes to edit widget css
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}) 
        }