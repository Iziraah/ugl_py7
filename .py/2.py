# Напишите функцию группового переименования файлов.
# Она должна:
# принимать параметр - желаемое конечное имя файлов.
# при переименовании, в конце имени добавляется порядковый номер.
# принимать параметр - количество цифр в порядковом номере.(&!)
# принимать параметр - расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# Принимать параметр - расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
# например, для диапазона [3,6] берутся буквы с третьей по шестую из исходного имени файла.
# к ним прибавляется желаемое конечное имя, если оно передано. далее, счетчик файлов и расширение.
# соберите из созданных на уроке и рамках дз ф-ций пакет для работы с файлами


import os


path = 'C:/Users/Маша/Desktop/домашка/пайтон угл/7'
def remane_file(extention: str, new_name: str, new_extention: str, diapazon: int): 
    # diapazon = [3,6]
    a,b = diapazon[0],diapazon[1]
    count = 0
    # new_name = new_name + count   
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            ext = os.path.splitext(filename)[1] # получили расширение
            n = os.path.splitext(filename)[0] # получили имя
            name_wd = n[a:b]
            if (ext == extention):
                count_str = str(count)
                new_name2 = new_name + count_str + new_extention # для переданного имени
                # new_name2 = name_wd + count_str + new_extention # новое имя: имя+счетчик+расширение
                file_new_name = os.path.join(path, new_name2)
                os.rename(filename, file_new_name)
                count +=1

remane_file('.pdf', 'test', '.txt', [3,6])


