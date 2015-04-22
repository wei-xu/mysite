from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django import forms
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from intern.models import Blog, Document
from intern.forms import DocumentForm, BlogForm
# Create your views here.
def index(request):
	blogs = Blog.objects.order_by('-publish_time')[:6]
	documents = Document.objects.order_by('-upload_time')[:3]
	latest_file_list = {}
	latest_blog_list = {}
	for document in documents:
		latest_file_list[document.docfile.name.split('/')[-1]] = document
	for blog in blogs:
		latest_blog_list[blog.title] = blog.content[:20]
	context = {
            'latest_blog_list': latest_blog_list,
            'latest_file_list': latest_file_list,
            }
	# dictionary key refers to the variable in {{}} of the same name.
	return render(request, 'intern/index.html', context)
	# test github syncronization

def index_detail(request):
	latest_blog_list = Blog.objects.order_by('-publish_time')[:]
	context = {'latest_blog_list': latest_blog_list}
	# dictionary key refers to the variable in {{}} of the same name.
	return render(request, 'intern/study_center.html', context)

def file_center(request):
	# Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('intern:file_center'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    file_list = {}
    for document in documents:
        file_list[document.docfile.name.split('/')[-1]] = document

    # Render list page with the documents and the form
    return render_to_response(
        'intern/file_center.html',
        {'documents': documents, 'form': form, 'file_list': file_list},
        context_instance=RequestContext(request),
    )
	#return render(request, 'intern/file_center.html')

class DetailView(generic.DetailView):
	"""docstring for DetailView"""
	model = Blog
	template_name = 'intern/detail.html'		


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
			return HttpResponseRedirect(reverse('intern:study_center'))
	else:
		form = BlogForm()
	return render(request, 'intern/add_blog.html', {'form':form})


def add_file(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'], uploader=form.uploader)
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('intern:add_file'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    file_list = {}
    for document in documents:
        file_list[document.docfile.name.split('/')[-1]] = document

    # Render list page with the documents and the form
    return render_to_response(
        'intern/add_file.html',
        {'documents': documents, 'form': form, 'file_list': file_list},
        context_instance=RequestContext(request),
    )
