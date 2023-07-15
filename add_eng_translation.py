import re
import argparse


def update_translation(source_file_name, translation_file_name):
    # Создание словаря для хранения пар "русский текст" - "английский текст"
    translations = {}

    # Открытие файла с переводами и чтение его строк
    with open(translation_file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Прохождение по каждой строке файла перевода
    for line in lines:
        # Попытка найти английский текст в строке
        translation_match = re.search(r'"([A-Za-z\s][^"]*)"', line)
        # Попытка найти русский текст в строке
        new_russian_text = re.search(r'(?:#|old).*?"([^"]*)"', line)

        # Если русский текст найден, сохраняем его
        if new_russian_text:
            russian_text = new_russian_text.group(1)

        # Если есть русский текст и соответствующий ему английский текст, добавляем их в словарь переводов
        if translation_match and russian_text:
            translations[russian_text] = translation_match.group(1)
            russian_text = None

    # Открытие исходного файла для чтения его строк
    with open(source_file_name, 'r', encoding='utf-8') as f:
        source_lines = f.readlines()

    # Открытие исходного файла для записи обновленных строк
    with open(source_file_name, 'w', encoding='utf-8') as f:
        # Прохождение по каждой строке исходного файла
        for line in source_lines:
            # Попытка найти русский текст в строке
            russian_text_match = re.search(r'^(?!.*(#|old)).*\"([А-Я][^\"]*)\"', line)

            # Если русский текст найден
            if russian_text_match:
                # Извлечение русского текста из найденного совпадения
                russian_text = russian_text_match.group(2)
                # Если русский текст есть в словаре переводов
                if russian_text in translations:
                    # Замена русского текста на английский в строке
                    new_line = line.replace(russian_text, translations[russian_text])
                    # Запись новой строки в файл
                    f.write(new_line)
                else:
                    # Если русского текста нет в словаре переводов, запись исходной строки в файл
                    f.write(line)
            else:
                # Если русского текста нет в строке, запись исходной строки в файл
                f.write(line)


if __name__ == "__main__":
    # Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser(description='Update translations in file.')
    parser.add_argument('source_filename', help='Source file to update')
    parser.add_argument('translation_filename', help='Translation file to be used')
    # Получение аргументов командной строки
    args = parser.parse_args()

    update_translation(args.source_filename, args.translation_filename)
