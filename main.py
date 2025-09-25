import string

def words_to_dict(words):
    for word in split_text:
        if word not in words_counter_dict:
            words_counter_dict[word] = 1
        else:
            words_counter_dict[word] += 1

    return words_counter_dict


def vowels_counter(text):
    vowels = 0

    for letter in text:
        if letter in vowels_list:
            vowels += 1

    return vowels

def clear_text(text):
    for letter in text:
        if letter in sign_list:
            text = text.replace(letter, '')

    return text


sign_list = string.punctuation

vowels_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

words_counter_dict = {}

text = input("Введите текст: ").lower()
#text = "Нет, нет, нет! Это невозможно. Почему? Почему так происходит? Жду, жду, жду ответа...".lower()

split_text = str(clear_text(text)).lower().split()

print(f'Количество слов в тексте: {len(split_text)}')

print(f'Самое длинное слово в тексте: {max(split_text, key=len)}')

print(f'Количество гласных в тексте: {vowels_counter(text)}')

print(f'Слова и частота их повторений в тексте: {words_to_dict(split_text)}')