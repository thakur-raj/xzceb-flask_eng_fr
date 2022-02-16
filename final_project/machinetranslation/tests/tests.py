"""
English-French Translation Application Tests
Author: Raj Thakur
"""
import unittest
import sys
sys.path.append("..")

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    Class to test the functions of translator
    """
    def test_null_english_to_french(self):
        """ Function to test the english_to_french translation when input is null"""
        self.assertIsNone(english_to_french(None))

    def test_null_french_to_english(self):
        """ Function to test the french_to_english translation when input is null"""
        self.assertIsNone(french_to_english(None))

    def test_english_to_french(self):
        """ Function to test the english to french translation"""
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        """ Function to test the french to english translation"""
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()
