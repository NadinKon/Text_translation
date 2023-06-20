import re
import argparse


def update_translation(file_name):
    translations = {}
    x = []
    russian_text = None
    c = []

    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()


    for line in lines:
        translation_match = re.search(r'"([A-Z][^"]*)"', line)
        new_russian_text = re.search(r'# *.*\.*.* "([^"]*)"', line)

        if new_russian_text:
            russian_text = new_russian_text.group(1)

        if russian_text and translation_match:
            translations[russian_text] = translation_match.group(1)
            russian_text = None  # reset the Russian text
    #print(translations)


    with open(file_name, 'w', encoding='utf-8') as f:
        for line in lines:
            #russian_text = re.search(r'# "([^"]*)"', line)
            russian_text = re.search(r'(?<!#) [a-z]* "([А-Я][^"]*)"', line)
            if russian_text and russian_text.group(1) in translations:
                new_line = line.replace(russian_text.group(1), translations[russian_text.group(1)])
                f.write(new_line)
            else:
                f.write(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update translations in file.')
    parser.add_argument('filename', help='File to update')
    args = parser.parse_args()

    update_translation(args.filename)
