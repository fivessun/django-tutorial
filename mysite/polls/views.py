from django import http
from django import shortcuts
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
    response = "You're looking at the results of question %s."
    return http.HttpResponse(response % question_id)


def vote(request, question_id):
    return http.HttpResponse("You're voting on question %s." % question_id)
