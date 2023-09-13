from django import urls

from polls import views

# For namespacing. If you use app_name, you have to annotate app name in html.
app_name = "polls"
urlpatterns = [
    urls.path("", views.index, name="index"),
    urls.path("<int:question_id>/", views.detail, name="detail"),
    urls.path("<int:question_id>/results/", views.results, name="results"),
    urls.path("<int:question_id>/vote/", views.vote, name="vote"),
]
