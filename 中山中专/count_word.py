def count_word_occurrences(sentence):
    word_list = sentence.lower().split()
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
sentence = "Hello world, hello python, hello world"
result = count_word_occurrences(sentence)
print(result)
