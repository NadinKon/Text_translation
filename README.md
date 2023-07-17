## Text_translation
Скрипт для проверки и редактирования перевода рус/англ в файлах с текстом.

### Установка
Клонируйте репозиторий https://github.com/NadinKon/Text_translation <br>

### Использование
Запустить скрипт process_rpy можно из терминала с указанием пути к файлу или файлам(через пробел), который нужно обработать. <br>

Например: python process_rpy.py C:\\Users\\Nadin\\Desktop\\test\\test\\input.rpy (process_rpy.py - название файла со скриптом, C:\\Users\\Nadin\\Desktop\\test\\test\\input.rpy - путь к файлу, в котором нужно сделать редактирование перевода) <br>

Если файлов несколько, пример: python script.py input1.rpy input2.rpy <br>

На выходе получается тот же файл, что и подается в аргументах, только с изменениями.

### add_eng_translation
Скрипт для замены всех фраз на дефолтный английский язык.

### Использование
Запустить скрипт можно из терминала с указанием пути к файлам(через пробел), которые нужно обработать.

Например: python add_eng_translation.py C:\Users\Nadin\Desktop\p_chapter_2.rpy C:\Users\Nadin\Desktop\e_chapter_2.rpy

(check_translation_rus-eng.py - название файла со скриптом,
 C:\Users\Nadin\Desktop\p_chapter_2.rpy - путь к файлу, в котором нужно сделать редактирование перевода C:\Users\Nadin\Desktop\e_chapter_2.rpy - путь к файлу, из которого берем перевод)

На выходе получается тот же файл, что и подается в аргументах, только с изменениями.
