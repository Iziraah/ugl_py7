
# напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float, разделены вертикальной чертой.
# Минимальное число = -1000, максимальное = +1000.
# Количество строк и имя файла передаются как аргументы функции.


import pathlib
from random import randbytes, randint, uniform, choices
import random
import shutil


def write_random(filename: str, count_lines: int) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(count_lines):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num:>5} | {float_num:.3f}\n')
# write_random('my_file',20)

# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохранить в файл.


VOWELS = 'аеиоуяюёэы'
CONSONANTS = ''.join([chr(ch) for ch in range(
    ord('а'), ord('я') + 1) if chr(ch) not in VOWELS])


def make_random_name(amount_of_names: int):
    count = 0
    all_names = []
    while count != amount_of_names:
        word_len = randint(4, 7)
        word = random.choices(VOWELS + CONSONANTS, k=word_len)
        if any(ch in VOWELS for ch in word):
            all_names.append(''.join(word).capitalize() + '\n')
            count += 1
    with open('names.txt', 'a', encoding='utf-8') as f:
        f.writelines(all_names)

# make_random_name(10)

# напишите функцию, которая открывает на чтение созданные файлы с числами и именами.
# перемножьте пары чисел. в новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строяными буквами и произведение по модулю.
# если результат умножения положительный, сохраните имя прописными буквами и произведение, округленное до целого.
# в результирующем файле должно быть столько же строк, сколько в более длинном файле.
# при достижении конца более короткого файла, возвращайтесь в его начало.


def whatever():
    with (open('my_file', 'r', encoding='utf-8') as fnumbers,
          open('names.txt', 'r', encoding='utf-8') as fnames):
        numbers = fnumbers.readlines()
        names = fnames.readlines()

    lines_to_write= []
    length_of_longest = max(len(numbers), len(names))
    for i in range(length_of_longest):
        two_numbers = numbers[i % len(numbers)]
        a, b = map(float, two_numbers.split('|'))
        mult = a*b

        name = names[i % len(names)]
        if mult >=0:
            lines_to_write.append(f'{name.upper().rstrip()}; {round(mult)}\n')
        else:
            lines_to_write.append(f'{name.lower().rstrip()}; {abs(mult)}\n')

    with open('endfile.txt','w', encoding='utf-8') as f:
        f.writelines(lines_to_write)
# whatever()

# создайте ф-цию, которая создает файл с указанным расширением.
# Функция принимает следующие параметры:
# -расширение
# - минимальная длина случайно сгенерированного имени, по умолчанию 6
# - максимальная длина случайно сгенерированного имени, по умолчанию 30
# - максимальное число случайных байт, записанных в файл, по умолчанию 256
# - максимальное число случайных байт, записанных в файл, по умолчанию 4096
# - количество файлов, по умолчанию 42
# имя файла и его размер должны быть в рамках переданного диапазона.

from string import ascii_letters

def create_file(extension: str, min_len_name: int = 6,max_len_name: int = 30,
                min_size_file: int = 256, max_size_file: int = 4096,
                 amount_file: int = 2 ) -> None:
    for _ in range(amount_file):
        len_name = randint(min_len_name, max_len_name)
        file_name = ''.join(choices(ascii_letters, k = len_name)) + extension
        size = randint(min_size_file, max_size_file)
        with open(file_name, 'wb') as f:
            f.write(randbytes(size))

# create_file('.txt')

# доработайте предфдущую задачу.
# создайте новую функцию, которая генерирует файлы с разным расширениями.
# расширения и количество файлов функция принимает в качестве параметров.
# количество переданных расширений может быть любым.
# количество файлов для каждого расширения различно.
# внутри используйте вызов ф-ции из прошлой задачи.

def gen_files(data: dict):
    for key, val in data.items():
        create_file(key, amount_file=val)

my_dict = {
    '.txt':6,
    # '.doc':5,
    # '.bin':5,
    # '.pdf':4
}

gen_files(my_dict)

# дорабатываем функции из предыдущих задач:
# генерируйте файлы в указанную директорию - отдельный параметр ф-ции.
# отсутствие/наличие директории не должно вызывать ошибок в работе ф-ции
# (добавьте проверки)
# Существующие файлы не должны удаляться/изменяться, в случае мовпадения имен.

from pathlib import Path
import os

def create_dir(name_dir: str):
    name = Path(Path.cwd() / name_dir)
    if not name.exists():
        name.mkdir()
    os.chdir(name)
    gen_files(my_dict)

# create_dir('other')

# создайте функцию для сортировки файлов по директориям.
# каждая группа включает файлы с несколькими расширениями.
# в исходной папке должны оствться только те файлы, которые не подошли для сортировки.

# получ расширение -> ext = os.path.splitext(file_name)[1]

path = 'C:/Users/Маша/Desktop/домашка/пайтон угл/7'
def make_dir_and_remove():
    new_path = ''
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            ext = os.path.splitext(filename)[1] # получаем расширение файлов
            if (os.path.exists(ext) != True and os.path.exists(ext) != '.py'): # создаем папки
                os.mkdir(ext)
            if (os.path.exists(ext) == True):
                new_path= os.path.abspath(ext) # получили путь к папке
                old_path = os.path.abspath(f) # путь к файлу
                shutil.copy2(f,new_path)
                os.remove(f)

make_dir_and_remove()


