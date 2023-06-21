import re
import argparse


def update_translation(file_name):
    # Создаем словарь для хранения соответствий между русскими фразами и их переводами на английский
    translations = {}
    russian_text = None

    # Открываем файл для чтения
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Проходимся по каждой строке в файле
    for line in lines:
        # Ищем английский текст
        translation_match = re.search(r'"([A-Z][^"]*)"', line)
        # Ищем русский текст
        new_russian_text = re.search(r'# *.*\.*.* "([^"]*)"', line)
        # Если нашли русский текст, сохраняем его
        if new_russian_text:
            russian_text = new_russian_text.group(1)
        # Если у нас есть русский текст и его перевод, добавляем их в словарь
        if russian_text and translation_match:
            translations[russian_text] = translation_match.group(1)
            russian_text = None  # сбрасываем значение русского текста после его сохранения
    # Открываем файл для записи
    with open(file_name, 'w', encoding='utf-8') as f:
        # Проходимся по каждой строке в файле
        for line in lines:
            # Ищем русский текст
            russian_text = re.search(r'(?<!#) [a-z]* "([А-Я][^"]*)"', line)
            # Если нашли русский текст и он есть в словаре переводов
            if russian_text and russian_text.group(1) in translations:
                # Заменяем русский текст на английский в этой строке
                new_line = line.replace(russian_text.group(1), translations[russian_text.group(1)])
                f.write(new_line)
            else:
                # Если русского текста нет, или его перевод не найден, записываем строку без изменений
                f.write(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update translations in file.')
    parser.add_argument('filename', help='File to update')
    args = parser.parse_args()

    update_translation(args.filename)
