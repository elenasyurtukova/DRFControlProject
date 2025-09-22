from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from usefulthings.models import Wont

from users.serializers import UserSerializer


class WontSerializer(ModelSerializer):
    class Meta:
        model = Wont
        fields = "__all__"
        read_only_fields = ['id', 'owner']

    def validate(self, attrs):
        wont = Wont(**attrs)
        wont.owner = self.context['request'].user
        wont.clean()
        return attrs
