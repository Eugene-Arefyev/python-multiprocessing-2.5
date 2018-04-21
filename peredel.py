# библиотека для подпроцессов
import subprocess
# библиотека для доступа к api ОС
import os
# библиотека для перемещения файлов
import shutil

# alt+1 - открыть project manager
# точка входа
from pathlib import Path

if __name__ == "__main__":
    # массив с именами входных файлов
    inItems = ['input.jpg', 'input1.jpg', 'input2.jpg']
    # массив с именами выходных файлов
    outItems = ['output1.jpg', 'output2.jpg', 'output3.jpg']
    # запускем подспроцесс и сохраняем в переменной process
    for i in range(0, inItems.__len__()):
        subprocess.call(['convert.exe', inItems[i], '-resize', '200', outItems[i]])
        # текущая папка где лежи скрипт
        directory = os.path.dirname(__file__)
        # откуда копировать файл изображения
        src = r'{}/{}'.format(directory, outItems[i])
        # куда копировать файл
        dst = r'{}/result/{}'.format(directory, outItems[i])
        # конеченая директория изображения - путь до нее
        directory = r'{}/result'.format(directory)
        # проверка существует ли папка results
        if not os.path.exists(directory):
            os.makedirs(directory)
        # перемещение файла
        my_file = Path(src)
        if my_file.exists():
            shutil.move(src, dst)
