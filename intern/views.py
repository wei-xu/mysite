from django.shortcuts import render, get_object_or_404
from django.views import generic

from intern.models import Blog
# Create your views here.
def index(request):
	latest_blog_list = Blog.objects.order_by('-publish_time')[:]
	context = {'latest_blog_list': latest_blog_list}
	return render(request, 'intern/index.html', context)

class DetailView(generic.DetailView):
	"""docstring for DetailView"""
	model = Blog
	template_name = 'intern/detail.html'		