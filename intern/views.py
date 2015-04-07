from django.shortcuts import render, get_object_or_404
from django.views import generic

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