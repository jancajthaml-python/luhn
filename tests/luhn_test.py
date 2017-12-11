import os, sys
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import luhn

class TestLuhn(unittest.TestCase):

  def test_digit(self):
    tests = [
      ("00123014764700968321002", 4),
      ("xy-1", None)
    ]

    for t in tests:
      number, expected = t
      valid = luhn.digit(number)
      self.assertEqual(valid, expected, "luhn.digit?(%(number)s) == %(valid)s, expected %(expected)s" % locals())

  def test_validate(self):
    tests = [
      ("001230147647009683210024", True),
      ("1234567812345678", False),
      ("xy-1", False)
    ]

    for t in tests:
      number, expected = t
      valid = luhn.validate(number)
      self.assertEqual(valid, expected, "luhn.validate?(%(number)s) == %(valid)s, expected %(expected)s" % locals())

  def test_generate(self):
    tests = [
      ("00123014764700968321002", "001230147647009683210024")
    ]

    for t in tests:
      number, expected = t
      valid = luhn.generate(number)
      self.assertEqual(valid, expected, "luhn.generate?(%(number)s) == %(valid)s, expected %(expected)s" % locals())

if __name__ == '__main__':
  unittest.main()
