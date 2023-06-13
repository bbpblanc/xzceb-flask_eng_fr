'''
Translator from and to English and French
'''
from deep_translator import MyMemoryTranslator

def englishToFrench(text: str) -> str:
    """
       Translate from English to French
    """
    translator = MyMemoryTranslator(source = "en", target = "fr")
    fr_text = translator.translate(text = text)
    return fr_text

def frenchToEnglish(text: str) -> str:
    """
       Translate from French to English
    """
    translator = MyMemoryTranslator(source = "fr", target = "en")
    en_text = translator.translate(text = text)
    return en_text


if __name__ == "__main__":
    words = ["Hello how are you today?", "I'm going well, thank you", "Hello"]
    for w in words:
        print(f"{w} -> {englishToFrench(w)}")

    words = ["Comment allez-vous?", "Je vais bien merci, quelle heure est-il?"]
    for w in words:
        print(f"{w} -> {frenchToEnglish(w)}")
