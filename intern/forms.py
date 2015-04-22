# -*- coding: utf-8 -*-
from django import forms
from intern.models import Document, Blog

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