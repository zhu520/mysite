from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.template import loader
# from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		''' Return the last five published questions. '''
		return Question.objects.order_by('-pub_date')[:5]
'''
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	# return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)

	# output = ', '.join([q.question_text for q in latest_question_list])
	# return HttpResponse(output)
	
	# return HttpResponse("Hello, world. You're at the polls index.")
'''

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
'''
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)

	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")

	return render(request, 'polls/detail.html', {'question': question})

	# return HttpResponse("You're looking at question %s." % question_id)
'''

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
'''
def results(request, question_id):
	# response = "You're looking at the results of question %s."
	# return HttpResponse(response % question_id)
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})
'''

def vote(request, question_id):
	# return HttpResponse("You're voting on question %s." % question_id)
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		# 竞争条件 error 健壮性
		selected_choice = Choice.objects.get(pk=request.POST['choice'])
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

