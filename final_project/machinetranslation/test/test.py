import unittest
from translator import englishToFrench,frenchToEnglish

class testTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

if __name__=='__main__':
    unittest.main()
