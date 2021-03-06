from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Snippet
from ..serializers import SnippetSerializer

__all__ = (
    'SnippetList',
    'SnippetDetail',
)


class SnippetList(APIView):
    # /snippets/ <- 에 매칭되도록 urls모듈 작성
    #                   app_name이 'snippets'여야 함
    #
    # config.urls
    #   include('snippets.urls')
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #        serializer.delete()
    #        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    #     return Response(status=status.HTTP_400_BAD_REQUEST


class SnippetDetail(APIView):
    def get_object(self, pk, format=None):
        return get_object_or_404(Snippet, pk=pk)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
