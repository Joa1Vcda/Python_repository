"""split/join strings in python"""

phrase = "look this,    that thing is interessant"

list_words = phrase.split()
print(list_words)

division_phrase = phrase.split(", ")
print(division_phrase)

list_phrase = []
for i, frase in enumerate(division_phrase):
    # print(division_phrase[i].lstrip())
    list_phrase.append(division_phrase[i].strip())

print(division_phrase)
print(list_phrase)

joined_sentences = "-".join(list_phrase)
print(joined_sentences)
