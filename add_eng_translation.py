import re
import argparse


def update_translation(source_file_name, translation_file_name):
    # Создаем словарь для хранения переводов
    translations = {}
    russian_text = None

    # Открываем файл с переводами
    with open(translation_file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Обрабатываем каждую строку в файле
    for line in lines:
        # Ищем английский текст в строке
        translation_match = re.search(r'"([A-Z][^"]*)"', line)
        # Ищем русский текст в строке
        new_russian_text = re.search(r'# *.*\.*.* "([^"]*)"', line)

        # Если нашли русский текст, сохраняем его
        if new_russian_text:
            russian_text = new_russian_text.group(1)

        # Если есть русский текст и его перевод, сохраняем их в словаре
        if russian_text and translation_match:
            translations[russian_text] = translation_match.group(1)
            russian_text = None

    # Открываем исходный файл
    with open(source_file_name, 'r', encoding='utf-8') as f:
        source_lines = f.readlines()

    # Записываем обновленный текст обратно в исходный файл
    with open(source_file_name, 'w', encoding='utf-8') as f:
        # Обрабатываем каждую строку в исходном файле
        for line in source_lines:
            # Ищем русский текст в строке
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
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Update translations in file.')
    parser.add_argument('source_filename', help='Source file to update')
    parser.add_argument('translation_filename', help='Translation file to be used')
    # Получаем аргументы командной строки
    args = parser.parse_args()

    # Вызываем функцию обновления перевода с переданными аргументами
    update_translation(args.source_filename, args.translation_filename)
