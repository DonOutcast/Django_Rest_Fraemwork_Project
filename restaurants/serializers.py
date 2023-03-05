from rest_framework import serializers
from .models import Mac


class MacSerializers(serializers.ModelSerializer):
    menu = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="menu-detail"
    )

    class Meta:
        model = Mac
        fields = (
            "menu"
        )
