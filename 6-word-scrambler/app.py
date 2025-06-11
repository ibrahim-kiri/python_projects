import random

print("📝 WORD SCRAMBLER 📝")

while True:
    word = input("\nEnter a word to scramble (or quit): ")
    if word.lower() == "quit":
       print("👋 Goodbye!")
       break
    # ["e","v","e","r","y","o","n","e"] => ["o","n","e,"e","r","y","e","v"] => oneeryev
    letters = list(word)
    random.shuffle(letters)
    print(f"Scrambled: {"".join(letters)}")