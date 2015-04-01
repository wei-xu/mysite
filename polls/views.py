from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
# from django.http import Http404
# from django.template import RequestContext, loader

from polls.models import Question, Choice

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]
# ================ old version 2 =============== #
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	context = {'latest_question_list': latest_question_list}
# 	# loading a template and render the template.
# 	return render(request, 'polls/index.html', context)
# 	# ======== old version 1 ========= #
# 	# template = loader.get_template('polls/index.html')
# 	# context = RequestContext(request, {
# 	# 	'latest_question_list': latest_question_list,
# 	# 	})
# 	# return HttpResponse(template.render(context))

# #	output = ','.join([p.question_text for p in latest_question_list])
# #	return HttpResponse(output)

class DetailView(generic.DetailView):
	"""docstring for DetailView"""
	model = Question
	template_name = 'polls/detail.html'
# =============== old version =============== #		
# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	# try:
# 	# 	question = Question.objects.get(pk=question_id)
# 	# except Question.DoesNotExist:
# 	# 	raise Http404("Question does not exist")
# 	return render(request, 'polls/detail.html', {'question': question})

class ResultsView(generic.DetailView):
	"""docstring for ResultsView"""
	model = Question
	template_name = 'polls/results.html'
# ============================
# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': p,
			'error_message': "You didn't select a choice."
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
		# This line of code helps us redirect to page results to see the 
		# result of question[id].
	# return HttpResponse("You're voting on question %s." % question_id)