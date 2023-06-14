from django.test import TestCase
from core.models import Pessoa
from core.forms import formProf

class MyFormTestCase(TestCase):
    def test_valid_form_submission(self):
        form_data = {"nome": "Test", "professor":"Test"}
        form = formProf(data=form_data)
        self.assertTrue(form.is_valid())

class MyModelTestCase(TestCase):
    def test_model_creation(self):
        obj = Pessoa.objects.create(nome="Test")
        self.assertEqual(obj.nome, "Test")

