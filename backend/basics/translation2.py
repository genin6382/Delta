from googletrans import Translator
translator=Translator()
text=input("enter your sentence : ")
inp=input("Enter the language code of preferred language:")

print("This sentence translates to :",translator.translate(text,dest=inp).text)