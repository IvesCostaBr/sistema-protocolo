from django.test import TestCase
from protocolo.models import Protocolo

class ProtocoloTestCase(TestCase):
    def setUp(self):
        Protocolo.objects.create(titulo='halow', bio='alow')
        Protocolo.objects.create(titulo='halow', bio='alow')

    def test_veifica_banco_vazio(self):
        assert Protocolo.objects.all().count() != 0