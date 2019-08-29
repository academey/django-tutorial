from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone


class IndexView(generic.ListView):
    # default template name is polls/question_list.html
    template_name = 'polls/index.html'

    # default context var is question_list
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # 미래의 Question 은 아예 검색이 안 되도록 만든다. 아니 근데 이럴거면 애초에
    # Question model 자체 default 규모에 설정하는 게 나을듯
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    # default context var is question
    model = Question

    # default template name is polls/question_detail.html
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    # default context var is question
    model = Question

    # default template name is polls/question_detail.html
    template_name = 'polls/results.html'

def vote(request, question_id):
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
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
