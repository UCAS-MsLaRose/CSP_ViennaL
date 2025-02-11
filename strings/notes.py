# Vienna LaRose, Strings Notes Python

#string is a data type that holds any info surround by quotation marks "" ''

note ="Vienna's class"

#name = input("What is your first name?\n").strip().capitalize()

#print(f"Hello {name} welcome to my program!")
#print("this is your name "+ name)

sentence = "The quick brown fox jumps over the lazy dog."

#print(len(sentence))
#print(sentence[4])
start = sentence.find("brown")
length = len("brown fox")
print(sentence[start:start+length])