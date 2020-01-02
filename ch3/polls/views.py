from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Question


from django.views.generic import ListView

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list} #python 사전 type으로 data 전달
#     return render(request, 'polls/index.html', context)

class IndexView(ListView):
    model = Question
    context_object_name = 'latest_question_list'
    template_name = 'polls/index.html'

    def get_queryset(selt):
        return Question.objects.order_by('-pub_date')[:5]

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #filter가능 ,list 비어있으면 error
    return render(request, 'polls/detail.html', {'question': question})
    #넘어온 params에 맞는 question을 불러온다.

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        #reverse 함수는 url 패턴명으로부터 url 스트링을 구할 수 있음
