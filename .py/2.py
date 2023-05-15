# Напишите функцию группового переименования файлов.
# Она должна:
# принимать параметр - желаемое конечное имя файлов.
# при переименовании, в конце имени добавляется порядковый номер.
# принимать параметр - количество цифр в порядковом номере.
# принимать параметр - расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# Принимать параметр - расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
# например, для диапазона [3,6] берутся буквы с третьей по шестую из исходного имени файла.
# к ним прибавляется желаемое конечное имя, если оно передано. далее, счетчик файлов и расширение.
# соберите из созданных на уроке и рамках дз ф-ций пакет для работы с файлами

# def gen_files(data: dict):
#     for key, val in data.items():
#         create_file(key, amount_file=val)

# my_dict = {
#     '.txt':6,
#     '.doc':5,
#     '.bin':5,
#     '.pdf':4
# }

# gen_files(my_dict)

import os


path = 'C:/Users/Маша/Desktop/домашка/пайтон угл/7'
def remane_file(extention: str, new_name: str): 
    count = 0
    # new_name = new_name + count   
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            ext = os.path.splitext(filename)[1] # получили расширение
            if (ext == extention):
                new_name = new_name + str(count)
                file_new_name = os.path.join(path, new_name)
                os.rename(filename, file_new_name)
                count = int(count)
                count +=1

remane_file('.txt', 'test')