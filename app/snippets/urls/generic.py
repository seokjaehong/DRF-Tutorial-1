from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..apis import generic

urlpatterns = [
    path('', generic.SnippetList.as_view()),
    path('<int:pk>/', generic.SnippetDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
