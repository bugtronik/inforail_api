from rest_framework import serializers
from .models import SpErametVtrainMini

class SpErametVtrainMiniSerializer(serializers.Serializer):
    class Meta:
        model = SpErametVtrainMini
