# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os.path

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)


#file_path = "C:/Users/User/Documents/example.txt"
print(get_file_info('C:/Users/User/Documents/example.txt'))
print(get_file_info('/home/user/data/file'))
print(get_file_info('D:/myfile.txt'))

#print(get_file_info(file_path = 'C:/Users/User/Documents/example.txt')) #('C:/Users/User/Documents/', 'example', '.txt')

#print(get_file_info(file_path = '/home/user/data/file'))    #('/home/user/data/', '', '.file')
                                                             #('/home/user/data', 'file', '')
#print(get_file_info(file_path = 'D:/myfile.txt'))   #('D:/', 'myfile', '.txt')
