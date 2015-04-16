from django.shortcuts import render, get_object_or_404
from django import forms
from django.views import generic
from django.http import HttpResponseRedirect

from intern.models import Blog
# Create your views here.
def index(request):
	latest_blog_list = Blog.objects.order_by('-publish_time')[:]
	context = {'latest_blog_list': latest_blog_list}
	# dictionary key refers to the variable in {{}} of the same name.
	return render(request, 'intern/index.html', context)
	# test github syncronization

def index_detail(request):
	return render(request, 'intern/index_detail.html')


class DetailView(generic.DetailView):
	"""docstring for DetailView"""
	model = Blog
	template_name = 'intern/detail.html'		

# class BlogForm(forms.Form):
# 	title = forms.CharField()
class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['title', 'author', 'content']

def add_blog(request):
	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			# try:
			# 	form.save()
			# except:
			# 	return render(request, 'intern/add_blog.html', {
			# 		'error_message': "Connection failed",
			# 		'form': form,
			# 		})
			form.save()
			return HttpResponseRedirect('/intern/index_detail')
	else:
		form = BlogForm()
	return render(request, 'intern/add_blog.html', {'form':form})
	
