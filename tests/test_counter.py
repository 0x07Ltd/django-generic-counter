try:
    import unittest
except ImportError:
    import django.utils.unittest as unittest

from django_dynamic_fixture import G

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
