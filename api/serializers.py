from rest_framework.serializers import ModelSerializer

from .models import Url


class UrlSerializerIn(ModelSerializer):
    class Meta:
        model = Url
        fields = ["url"]

class UrlSerializerOut(ModelSerializer):
    class Meta:
        model = Url
        fields = "__all__"
