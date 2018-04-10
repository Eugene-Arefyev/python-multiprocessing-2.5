# библиотека для подпроцессов
import subprocess
# библиотека для доступа к api ОС
import os
# библиотека для перемещения файлов
import shutil
# alt+1 - открыть project manager
# точка входа
if name == "main":
    # запускем подспроцесс и сохраняем в переменной process
    process = subprocess.call(['convert.exe', 'input.jpg', '-resize', '200', 'output.jpg'])
    # текущая папка где лежи скрипт
    directory = os.path.dirname(file)
    # откуда копировать файл изображения
    src = r'{}/output.jpg'.format(directory)
    # куда копировать файл
    dst = r'{}/result/output.jpg'.format(directory)
    # конеченая директория изображения - путь до нее
    directory = r'{}/result'.format(directory)
    # проверка существует ли папка results
    if not os.path.exists(directory):
        os.makedirs(directory)
    # перемещение файла
    shutil.move(src, dst)