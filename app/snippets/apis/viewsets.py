from rest_framework import viewsets, permissions

from snippets.permission import IsOwnerOrReadOnly
from ..models import Snippet
from ..serializers import SnippetSerializer


class SnippetViewSet(viewsets.Modelviewset):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )