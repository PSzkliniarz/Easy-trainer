from PIL import Image
from django import forms
from .models import Comment, Image, Video

class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_text']

class AddImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['images', 'label']

class AddVideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['video', 'label']