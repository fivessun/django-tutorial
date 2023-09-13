from django import urls
from django.contrib import admin

urlpatterns = [
    urls.path("__debug__/", urls.include("debug_toolbar.urls")),
    urls.path("admin/", admin.site.urls),
    urls.path("polls/", urls.include("polls.urls")),
]
