from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django import forms
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
## to redirect iframe to its parent view, we need TemplateResponse
#  to load a middle html
from django.template.response import TemplateResponse
from django.forms.models import inlineformset_factory

from .models import Blog, Document, Wiki, WikiEditHistory, User
from .forms import DocumentForm, BlogForm, WikiForm, WikiEditHistoryForm, UserForm
# Create your views here.
def index(request):
    # homepage
    # get most recent 5 blogs and 3 documents from database
	blogs = Blog.objects.order_by('-publish_time')[:6]
	documents = Document.objects.order_by('-upload_time')[:3]
    # lists that need to be passed to the html.
	latest_file_list = []
	latest_blog_list = []
	for document in documents:
        # get the filename , file, file uploadtime
		latest_file_list.append((document.docfile.name.split('/')[-1],document, document.upload_time))
    # sort the file list according to time order
	latest_file_list = sorted(latest_file_list, key=lambda d:d[2], reverse=True)
    
	for blog in blogs:
        # get the blog title, blog summary, publish time, blog object
		latest_blog_list.append((blog.title, blog.content[:20], blog.publish_time, blog))
    # sort the blog list according to time order
	latest_blog_list = sorted(latest_blog_list, key=lambda x:x[2], reverse=True)
    # render the index.html with two lists
	context = {
            'latest_blog_list': latest_blog_list,
            'latest_file_list': latest_file_list,
            }
	# dictionary key refers to the variable in {{}} of the same name.
	return render(request, 'intern/index.html', context)
	# test github syncronization

def index_detail(request, blog_id=''):
    # study center page
    # get all the blogs 
	latest_blog_list = Blog.objects.order_by('-publish_time')
	context = {'latest_blog_list': latest_blog_list, 'blog_id': blog_id}
	# render the study_center.html page with context
	return render(request, 'intern/study_center.html', context)

def file_center(request):
    # file center page
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
    file_list_bak = {}
    file_list = []
    for document in documents:
        # file_list[document.docfile.name.split('/')[-1]] = (document, document.upload_time)
        file_list.append((document.docfile.name.split('/')[-1],document, document.upload_time))
    file_list = sorted(file_list, key=lambda d:d[2], reverse=True)

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
    # if the page is submitted
	if request.method == "POST":
        # get the form from the http POST
		form = BlogForm(request.POST)
		if form.is_valid():
            # BlogForm is a model form, form.save() will directly save 
            # the content in the form to the database
			form.save()
            # return to study_center after adding a blog
			# usually the following could be a substitute:

            # return HttpResponseRedirect(reverse('intern:study_center'))

            # but since the page is split into two subpages: left page and right
            # page, redirecting the right subpage to the parent page causes infinite 
            # recurrent redirection. Therefore we use a global redirection
            # 
            # google "django redirect to parent of iframe from view" for more info
			return TemplateResponse(request, 'intern/redirect_url.html', {'redirect_url': reverse('intern:study_center')})
	else:
        # show the form page
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

def wiki_index(request, wiki_pagename=''):
    if wiki_pagename:
        # failed when change to objects.filter(wiki_pagename=wiki_pagename)
        # page = Wiki.objects.get(wiki_pagename=wiki_pagename)
        # wiki_pagename should be unique
        page = get_object_or_404(Wiki, wiki_pagename=wiki_pagename)
        if page:
            # leave is_existing variable for the coming search function
            context = {'page': page, 'is_existing': True}
            return render(request, 'intern/wiki_page.html', context)
        else:
            context = {'page': page, 'is_existing': False}
            return render(request, 'intern/wiki_edit.html', context)
    else:
        wiki_list = Wiki.objects.all()
        context = {'wiki_list': wiki_list}
        return render(request, 'intern/wiki_index.html', context)

# def wiki_edit(request, wiki_pagename):
#     page = Wiki.objects.get(wiki_pagename=wiki_pagename)
#     context = {
#             'wiki_pagename': page.wiki_pagename,
#             'wiki_content': page.wiki_content,
#     }
#     return render(request, 'intern/wiki_edit.html', context)

def wiki_edit(request, wiki_pagename=''):
#   now the edit history function has been removed
#   form2 is not being used
    page = Wiki.objects.filter(wiki_pagename=wiki_pagename)
    if request.method == 'POST':
        form1 = WikiForm(request.POST)
        form2 = WikiEditHistoryForm(request.POST)
        if form1.is_valid():
            if page:                
                page[0].wiki_pagename = form1.cleaned_data['wiki_pagename']
                page[0].wiki_content = form1.cleaned_data['wiki_content']
                page[0].save()
                if form2.is_valid():
                    new_edit_record = WikiEditHistory(edit_reason=form2.cleaned_data['edit_reason'])
                    # set WikiEditHistory object's foreign key as pagename, not
                    # the other way around.
                    # for example, page.edit_reason = new_edit_record is wrong
                    new_edit_record.edit_pagename = page[0]
                    new_edit_record.save()
                return HttpResponseRedirect(reverse('intern:wiki_index', args=[form1.cleaned_data['wiki_pagename']]))
            else:
                # if page is null, automatically create a new page
                # this is for the coming search function
                new_page = Wiki(
                        wiki_pagename=form1.cleaned_data['wiki_pagename'],
                        wiki_content=form1.cleaned_data['wiki_content']
                    )
                new_page.save()
                # new_create_record = WikiEditHistory(
                #         edit_reason=form2.cleaned_data['edit_reason']
                #     )
                # new_create_record.edit_pagename = new_page
                # new_create_record.save()
                return HttpResponseRedirect(reverse('intern:wiki_index'))
        return HttpResponseRedirect(reverse('intern:wiki_index'))
    else:
        # show the page 
        if page:
            wikiForm = WikiForm(initial={'wiki_pagename': page[0].wiki_pagename, 'wiki_content': page[0].wiki_content})
        else:
            wikiForm = WikiForm()    
        wikiEditHistoryForm = WikiEditHistoryForm()
        context = {
                'wikiEditHistoryForm': wikiEditHistoryForm,
                'wikiForm': wikiForm,
                'wiki_pagename': wiki_pagename,
                'not_creating_page': page,
        }
        return render(request, 'intern/wiki_edit.html', context)

def wiki_view_history(request, wiki_pagename):
    page = Wiki.objects.get(wiki_pagename=wiki_pagename)
    history = WikiEditHistory.objects.filter(edit_pagename=page)
    context = {
            'history': history,
            'wiki_pagename': page.wiki_pagename,
    }
    return render(request, 'intern/wiki_view_history.html', context)

#Register
def regist(req):
    identify = True
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #Obtain form data
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #Add onto database
            user = User.objects.filter(username__exact = username)
            if user:
                identify = False
                return render_to_response('intern/regist.html', {'uf':uf, 'identify':identify},context_instance=RequestContext(req))
            else:
                User.objects.create(username= username,password=password)
                return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('intern/regist.html',{'uf':uf, 'identify':identify}, context_instance=RequestContext(req))

#Login
def login(req):
    identify = True
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #identify = True
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #Compare with database
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                response = HttpResponseRedirect(reverse('intern:index'))
                #Write username into broser, run-out time 3600 secs
                response.set_cookie('username',username,3600)
                return response
            else:
                identify = False
                return render_to_response('intern/login.html', {'uf':uf, 'identify':identify},context_instance=RequestContext(req))
    else:
        uf = UserForm()
    return render_to_response('intern/login.html',{'uf':uf, 'identify':identify},context_instance=RequestContext(req))

#Login successfully
def index1(req):
    username = req.COOKIES.get('username','')
    return render_to_response('intern/index.html' ,{'username':username})

#Logout
def logout(req):
    response = HttpResponse('logout !!')
    #clean up cookies
    response.delete_cookie('username')
    return response