from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        view_name='snippets:snippet-detail',
        many=True,
        read_only=True,
    )

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'snippets',
        )