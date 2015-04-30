# -*- coding: utf-8 -*-
from django import forms
from .models import Document, Blog, Wiki, WikiEditHistory

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
    # class Meta:
    # 	model = Document
    # 	fields = ['uploader']

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['title', 'author', 'content']
		# widgets = {
		# 	'content': forms.Textarea(attrs={'cols':50, 'rows':5}),
		# }

class WikiForm(forms.Form):
	wiki_pagename = forms.CharField(
					max_length=60,
					label='edit_pagename',
					widget=forms.TextInput(
						attrs={
							'class':'form-control',
							'id':'edit_pagename',
						}
						)
		)
	wiki_content = forms.CharField(label='editContent', 
								widget=forms.Textarea(attrs={'class':'form-control',
								'id':'editContent'}
								)
							)
	#　class Meta:
	#	model = Wiki
	#	fields = ['wiki_pagename', 'wiki_content']	

class WikiEditHistoryForm(forms.Form):
	edit_reason = forms.CharField(
		label='edit_reason',
		max_length=200,
		widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'id':'edit_reason'
			})
		)
	#class Meta:
	#	model = WikiEditHistory
	#	fields = ['edit_reason']

# --- Register and Login
# ---------------Register modules-----------------------------------
#Form
class UserForm(forms.Form): 
    username = forms.CharField(label='Username',max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'id':'inputUsername', 'placeholder':'Username'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','id':'inputPassword','placeholder':'Password'}))
