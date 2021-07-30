from django import forms
from .models import Comment,Post


class EmailPostForm(forms.Form):
     
	name	     =	forms.CharField(max_length=25,widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Name'}))
	email	=	forms.EmailField()
	to	     =	forms.EmailField()
	comments	=	forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.Form):
	name	=	forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class': 'form-control mt-2','placeholder':'Name'}))
	email	=	forms.EmailField()
	body	=	forms.CharField(widget=forms.Textarea(attrs={'class':"form-control mt-2" ,'placeholder':"Message", 'rows':"5"}))

	email.widget.attrs.update({'class': 'form-control mt-2','placeholder':'Email'})
	


class PostForm(forms.ModelForm):
	class Meta:
		model =Post
		fields =('title','body','status')
# class CommentForm(forms.ModelForm):
# 	class Meta:
# 		model = Comment
# 		fields = ('name','email','body')
    
