try:
    import unittest
except ImportError:
    import django.utils.unittest as unittest

from django_dynamic_fixture import G
from django.db import IntegrityError

from django_generic_counter.models import Counter


class CounterTestCase(unittest.TestCase):

    def test_counter_increment(self):
        """
        Assignment addition should increase the counter.
        """
        counter = G(Counter)
        self.assertEqual(int(counter), 0)
        counter += 10
        self.assertEqual(int(counter), 10)
        counter += 100
        self.assertEqual(int(counter), 110)

    def test_counter_decrement(self):
        """
        Assignment subtraction should decrease the counter.
        """
        counter = G(Counter)
        self.assertEqual(int(counter), 0)
        counter -= 10
        self.assertEqual(int(counter), -10)
        counter -= 100
        self.assertEqual(int(counter), -110)

    def test_counter_cast_to_int(self):
        """
        Casting an instance of a Counter should return an integer containing the count.
        """
        counter = G(Counter)
        counter.count = 1337
        self.assertEqual(int(counter), 1337)

    def test_counter_name_unique(self):
        """
        There can be only one.
        """
        Counter.objects.filter(name="Highlander").delete()
        Counter.objects.create(name="Highlander")
        self.assertRaises(IntegrityError, Counter.objects.create, name="Highlander")

    def test_set_count(self):
        """
        Should set the count immediately in the database and update the local value.
        """
        counter = G(Counter)
        counter.count = 1337
        counter.save()
        self.assertEqual(int(counter), 1337)
        self.assertEqual(int(Counter.objects.get(pk=counter.pk)), 1337)
        counter.set_count(101)
        self.assertEqual(int(counter), 101)
        self.assertEqual(int(Counter.objects.get(pk=counter.pk)), 101)
