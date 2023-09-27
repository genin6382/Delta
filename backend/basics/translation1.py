from googletrans import Translator
translator=Translator()
text=input("enter your sentence : ")
print("This sentence translates to :",translator.translate(text).text)