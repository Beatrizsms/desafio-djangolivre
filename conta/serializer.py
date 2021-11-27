from .models import Conta
from rest_framework import serializers

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Conta
        fields= ['agência', 'conta','saldo']
