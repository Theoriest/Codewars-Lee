test = ["Welcome","to","CodeWars","Hey fellow warriors","This sentence is a sentence"]

def spin_words(sentence):
    sn_list = sentence.split()
    result = []
    for word in sn_list:
        if len(word) >= 5:
            word = word[::-1]
            result.append(word)
        else:
            result.append(word)
    return " ".join(result)

for sentence in test:
    print(sentence)
    print(spin_words(sentence))