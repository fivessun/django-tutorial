from django import urls
from django.contrib import admin

urlpatterns = [
    urls.path("polls/", urls.include("polls.urls")),
    urls.path("admin/", admin.site.urls),
]
