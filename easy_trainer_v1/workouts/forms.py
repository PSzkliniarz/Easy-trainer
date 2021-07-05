from PIL import Image
from django import forms
from .models import Comment, Image

class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_text']

class AddImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['images']