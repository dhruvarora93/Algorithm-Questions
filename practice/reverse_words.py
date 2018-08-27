def reverse_words(words):
    words.reverse()
    start_index = 0
    for index, word in enumerate(words):
        if word == ' ' or index == len(words) - 1:
            end_index = index - 1
            if index == len(words) - 1:
                end_index = index
            while start_index < end_index:
                words[start_index], words[end_index] = words[end_index], words[start_index]
                start_index += 1
                end_index -= 1
            start_index = index + 1
    print(''.join(words))


reverse_words([ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ])