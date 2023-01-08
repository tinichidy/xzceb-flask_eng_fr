import unittest

from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
          def test_nullf2e(self): 
                    self.assertRaises(ValueError, french_to_english, None)
                    self.assertRaises(ValueError, english_to_french, None)

    
          def test_english_to_french(self):
                    self.assertEqual(english_to_french('Hello'), 'Bonjour')

          def test_french_to_english(self):
                    self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)