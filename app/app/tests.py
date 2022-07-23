from django.test import SimpleTestCase
from . import calc

class DjangoTestClass(SimpleTestCase):
    def test_add_number(self):
        res=calc.add(8,7)

        self.assertEqual(res,15)