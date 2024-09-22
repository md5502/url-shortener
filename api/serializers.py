from rest_framework import serializers

from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["full_url", "short_url", "counter", "created_at"]
        read_only_fields = ["short_url", "counter", "created_at"]

    def create(self, validated_data):
        # Create the Url object but don't save it yet
        url_instance = Url(**validated_data)
        url_instance.save()  # This triggers the short_url generation
        return url_instance
