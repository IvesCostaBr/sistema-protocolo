from .models import Contato
from rest_framework import serializers

class ContatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contato
        fields = ('nome', 'email', 'phone', 'message')
