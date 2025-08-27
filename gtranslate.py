from deep_translator import GoogleTranslator

# Inggris -> Indonesia
result = GoogleTranslator(source='en', target='id').translate("Hello Master, how are you?")
print(result)

# Indonesia -> Jepang
result2 = GoogleTranslator(source='id', target='ja').translate("Selamat malam")
print(result2)
