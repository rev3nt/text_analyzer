text = '''Дождь, дождь, дождь... Снова дождь. Лужи, лужи везде: на дороге, на тропинке, на асфальте.'''

vowels_counter = 0

sign_list = ['.', ',', '!', '?', ':', ';', '-', '—']

vowels_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю,' 'я']

words_counter_dict = {}

for s in sign_list: # Убираем знаки препинания
    text = text.replace(s, '')

split_text = text.lower().split() # Резделяем слова в массив, снижаем регистр

for word in split_text: # Проход по словам
    if word not in words_counter_dict: # Добавляем слова в словари и считаем их количество
        words_counter_dict[word] = 1
    elif word in words_counter_dict:
        words_counter_dict[word] += 1
    for letter in word: # Считаем гласные в каждом слове
        if letter in vowels_list:
            vowels_counter += 1

print(f'Количество слов в тексте: {len(split_text)}')

print(f'Самое длинное слово в тексте: {max(split_text)}')

print(f'Количество гласных в тексте: {vowels_counter}')

print(f'Слова и частота их повторений в тексте: {words_counter_dict}')