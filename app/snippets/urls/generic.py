from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..apis import generic

urlpatterns = [
    path('', generic.SnippetList.as_view(), name='snippet-list'),
    path('<int:pk>/', generic.SnippetDetail.as_view(), name='snippet-detail'),
    path('<int:pk>/highlight/',generic.SnippetHighlight.as_view(), name='snippet-highlight'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
