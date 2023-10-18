from rest_framework import serializers
from App_SAC import models


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'


class AtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Atendimento
        fields = '__all__'

