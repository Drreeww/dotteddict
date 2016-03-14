# standard imports
import unittest

from dotteddict import (
    dotteddict
)


class dotteddictTests(unittest.TestCase):
    """
    Test cases for the ``dotteddict`` class.
    """
    def test_set_value_where_key_starts_with_dot(self):
        # given
        data = {
            ".a": 1,
            "a.c": 2
        }
        # exercise
        # verify
        with self.assertRaises(ValueError):
            dotteddict(data)

    def test_set_value_where_key_ends_with_dot(self):
        # given
        data = {
            "a.": 1,
            "a.c": 2
        }
        # exercise
        # verify
        with self.assertRaises(ValueError):
            dotteddict(data)

    def test_set_values_with_the_same_base_key(self):
        # given
        data = {"a.b": 1,
                "a.c": 2,
                "a.c.d": 3,
                "a.c.e": 4}
        # verify
        with self.assertRaises(ValueError):
            dotteddict(data)

    def test_overlapping_by_substrings(self):
        # given
        items = ['a.b.c', 'a.a.a', 'a.b.e', 'a.a']
        # exercise
        # verify
        self.assertEquals(('a.a', 'a.a.a'), dotteddict._has_overlapped(items))

    def test_without_overlapping(self):
        """
        Test that passed items don't have a overlapping with the one of
        """
        # given
        items = ['a.b.c', 'a.a.d', 'a.b.e']
        # exercise
        # verify
        self.assertEquals((), dotteddict._has_overlapped(items))

    def test_underscores_not_overlapping(self):
        """
        Test that the passed items don't have overlapping members.
        """
        items = ["retries", "retries_again", "retries_foo"]
        self.assertEquals((), dotteddict._has_overlapped(items))

    def test_underscores_overlapping(self):
        items = ["retries", "retries_foo"]
        self.assertEquals(('retries', 'retries_foo'), dotteddict._has_overlapped(items, separator="_"))

    def test_dotted_get(self):
        value = "xyz"
        data = {"color": {"red": value}}

        dotted = dotteddict(data)

        self.assertEqual(dotted.get("color.red"), value)

    def test_dotted_attributes(self):
        value = "xyz"
        data = {"color": {"red": value}}

        dotted = dotteddict(data)

        self.assertEqual(dotted.color.red, value)

    def test_dotted_accessor(self):
        value = "X2940jkfa"
        data = {"rainbow": {"music": value}}

        dotted = dotteddict(data)

        self.assertEqual(dotted["rainbow.music"], value)

    def test_none_value(self):
        value = None
        data = {"rainbow": value}
        dotted = dotteddict(data)
        self.assertTrue(dotted.rainbow is value)

    def test_dotted_accessor_creation(self):
        key = "x.y.z"
        value = "foo"
        dotted = dotteddict({key: value})
        self.assertEqual(dotted[key], value)

    def test_missing_attribute_error(self):
        data = {"rainbow": None}
        dotted = dotteddict(data)

        with self.assertRaises(AttributeError):
            dotted.missing

    def test_setting_and_accessing(self):
        key = "x.y.z"
        value = 5
        dotted = dotteddict({key: value})

        self.assertEqual(dotted[key], value)
        self.assertEqual(dotted.x.y.z, value)

        message = "hello world"
        dotted.x.y.z = message
        self.assertEqual(dotted.x.y.z, dotted[key])
        self.assertEqual(dotted.x.y.z, message)
        self.assertEqual(dotted[key], message)

    def test_child_dictionary_types(self):
        key = "x.y.z"
        value = 5
        dotted = dotteddict({key: value})

        self.assertEqual(type(dotted.x), dotteddict)
        self.assertEqual(type(dotted.x.y), dotteddict)

    def test_child_dictionary_types_accessor(self):
        key = "x.y.z"
        value = 5
        dotted = dotteddict({key: value})

        self.assertEqual(type(dotted["x"]), dotteddict)
        self.assertEqual(type(dotted["x.y"]), dotteddict)
        self.assertEqual(type(dotted["x"]["y"]), dotteddict)

    def test_children_equivalence(self):
        key = "x.y.z"
        value = 5
        dotted = dotteddict({key: value})

        self.assertTrue(dotted.x is dotted["x"])
        self.assertTrue(dotted.x.y is dotted["x"]["y"])

    def test_construction_without_data(self):
        dotted = dotteddict()
        self.assertTrue(isinstance(dotted, dotteddict))
