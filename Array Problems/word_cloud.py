def split_words(input_string):
    words = []
    current_word_start_index = 0
    current_word_length = 0

    for i, char in enumerate(input_string):
        if char.isalpha() or char == '"' or char == '-':
            if current_word_length == 0:
                current_word_start_index = i
            current_word_length += 1
        else:
            word = input_string[current_word_start_index:
                                current_word_start_index + current_word_length]
            if word:
                words.append(word.lower())
            current_word_length = 0

    return words

print(split_words('After beating the eggs, Dana read the next step:\
Add milk and eggs, then add flour and sugar.'))


