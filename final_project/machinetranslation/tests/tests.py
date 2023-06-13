import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello how are you today?"), "Bonjour comment vas-tu aujourd'hui") 
        self.assertEqual(englishToFrench("I'm going well, thank you"), "Je vais bien, merci")  
        self.assertEqual(englishToFrench("Hello"), "Bonjour")  

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Comment allez-vous?"), "How are you?") 
        self.assertEqual(frenchToEnglish("Je vais bien merci, quelle heure est-il?"), "Thank you, what time is it?")  
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")  


unittest.main()
