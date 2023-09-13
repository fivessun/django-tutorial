from django import http
from django import shortcuts
from django import urls
from django.template import loader

from polls import models


def detail(request, question_id):
    if True:  # Shortcut
        question = shortcuts.get_object_or_404(models.Question, pk=question_id)
    else:
        try:
            question = models.Question.objects.get(pk=question_id)
        except models.Question.DoesNotExist:
            raise http.Http404("Question does not exist")
    return shortcuts.render(request, "polls/detail.html", {"question": question})


def index(request):
    latest_question_list = models.Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    if True:  # Shortcut
        return shortcuts.render(request, "polls/index.html", context)

    template = loader.get_template("polls/index.html")
    return http.HttpResponse(template.render(context, request))


def results(request, question_id):
    question = shortcuts.get_object_or_404(models.Question, pk=question_id)
    return shortcuts.render(request, "polls/results.html", {"question": question})


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
