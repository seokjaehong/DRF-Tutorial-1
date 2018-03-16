from rest_framework import serializers
from django.forms import widgets
from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
