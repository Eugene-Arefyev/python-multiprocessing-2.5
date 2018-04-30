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
    folder = 'Source'
    # текущая папка где лежи скрипт
    directory = os.path.dirname(__file__)
    # откуда копировать файл изображения
    src = r'{}/{}'.format(directory, folder)
    # текущий путь до скрипта
    currentFolder = r'{}'.format(directory, folder)
    if os.path.exists(src):
        # список файлов в диерктории
        files = os.listdir(src)
        # берем только изображения
        images = list(filter(lambda x: x.endswith('.jpg'), files))
        # конеченая директория изображения - путь до нее
        directory = r'{}/result'.format(directory)
        # подпроцесс
        for i in range(0, images.__len__()):
            subprocess.call(['convert.exe', folder + '\\' + images[i], '-resize', '200', images[i]])
            # куда копировать файл
            dst = r'{}/{}'.format(directory, images[i])

            # проверка существует ли папка results
            if not os.path.exists(directory):
                os.makedirs(directory)
            # перемещение файла
            my_file = Path(currentFolder + '\\' + images[i])
            if my_file.exists():
                shutil.move(currentFolder + '\\' + images[i], dst)
