import reverse
import unittest
import pytest

class TestReverse:
    def test_upper(self):
        assert "HELLO THERE BOB" == reverse.reverse_sentence("BOB THERE HELLO")

    def test_lower(self):
        assert "hello there bob" == reverse.reverse_sentence("bob there hello")

    def test_single(self):
        assert "HELLO" == reverse.reverse_sentence("HELLO")

    def test_camel(self):
        assert "Hello There Bob" == reverse.reverse_sentence("Bob There Hello")

    def test_punct(self):
        assert "HELLO THERE BOB!!" == reverse.reverse_sentence("BOB!! THERE HELLO")

class TestReverseUnit(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("HELLO THERE BOB", reverse.reverse_sentence("BOB THERE HELLO"))

    def test_lower(self):
        self.assertEqual("hello there bob", reverse.reverse_sentence("bob there hello"))

    def test_single(self):
        self.assertEqual("HELLO", reverse.reverse_sentence("HELLO"))

    def test_camel(self):
        self.assertEqual("Hello There Bob", reverse.reverse_sentence("Bob There Hello"))

    def test_punct(self):
        self.assertEqual("HELLO THERE BOB!!", reverse.reverse_sentence("BOB!! THERE HELLO"))

if __name__ == '__main__':
    unittest.main()
