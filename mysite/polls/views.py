from django import http
from django import shortcuts
from django import urls
from django.utils import timezone
from django.views import generic

from polls import models


class DetailView(generic.DetailView):
    model = models.Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return models.Question.objects.filter(pub_date__lte=timezone.now())


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return models.Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class ResultsView(generic.DetailView):
    model = models.Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = shortcuts.get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, models.Choice.DoesNotExist):
        return shortcuts.render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return http.HttpResponseRedirect(
            urls.reverse("polls:results", args=(question.id,))
        )
