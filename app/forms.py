from django import forms
from .models import Post,adress

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category','title', 'body','image1','image2','image3')

class adressform(forms.ModelForm):
    class Meta:
        model= adress
        fields=('state','district','taluko','village','pincode')
 
 