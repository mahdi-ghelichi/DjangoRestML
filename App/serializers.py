from rest_framework import serializers
from App.models import RFModel


class RFModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFModel
        fields = ('name', 'model')
