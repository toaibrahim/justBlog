from pyexpat import model
from turtle import title
from django import forms
from tinymce.widgets import TinyMCE
from .models import Comment,BlogModel
from marketing.models import Contact
  
  
class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
  
  
class PostForm(forms.ModelForm):
    
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )
    class Meta:
        model = BlogModel
        fields = ('title', 'content', 'image', 'category', 'featured', 'previous_post', 'next_post')
        exclude = ['user']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget = forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Type your comment',
        'id':'comment',
        'style':'background-color:transparent',
        'cols':'40',
        'rows':'5',
        'title':'title'
    }))
    class Meta:
        model = Comment
        fields = ('content',)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
