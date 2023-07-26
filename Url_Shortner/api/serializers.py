from rest_framework import serializers
from .models import Link

class LinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"