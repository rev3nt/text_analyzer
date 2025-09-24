def words_to_dict(words):
    for word in split_text:
        if word not in words_counter_dict:
            words_counter_dict[word] = 1
        elif word in words_counter_dict:
            words_counter_dict[word] += 1
    return words_counter_dict


def vowels_counter(words):
    vowels = 0

    for word in split_text:
        for letter in word:
            if letter in vowels_list:
                vowels += 1
    return vowels

def clear_text(text):
    for s in sign_list:
        text = text.replace(s, '')

    return text


sign_list = ['.', ',', '!', '?', ':', ';', '-', '—', '–', '‐', '(', ')', '[', ']', '{', '}',
                '"', "'", '`', '«', '»', '“','”', '‘', '’', '…', '/', '<', '>', '&', '*', '%',
                '#', '@', '$', '^', '~', '|', '+', '=', '_']

vowels_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

words_counter_dict = {}

text = input("Введите текст: ")

split_text = str(clear_text(text)).lower().split()

print(f'Количество слов в тексте: {len(split_text)}')

print(f'Самое длинное слово в тексте: {max(split_text, key=len)}')

print(f'Количество гласных в тексте: {vowels_counter(split_text)}')

print(f'Слова и частота их повторений в тексте: {words_to_dict(split_text)}')