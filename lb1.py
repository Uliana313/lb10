with open("story.txt", "w") as d:
    d.write("Our vacation\n")
    d.write("Every year we go to Florida. We like to go to the beach.\n")
    d.write("My favorite beach is called Emerson Beach. It is very long, with soft sand and palm trees.\n")
    d.write(" It is very beautiful. I like to make sandcastles and watch the sailboats go by.\n")

with open('story.txt', "r") as f:
    z = f.read()

words = z.split()
word_count = len(words)

unique_words = set(words)
unique_word_count = len(unique_words)

sentence_count = z.count('.') + z.count('!') + z.count('?')

with open('words.txt', 'w') as s:
    s.write(f"Кількість слів: {word_count}\n")
    s.write(f"Кількість унікальних слів: {unique_word_count}\n")
    s.write(f"Кількість речень: {sentence_count}\n")
