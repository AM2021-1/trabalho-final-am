from pdf2image import convert_from_path
import os
import shutil

def faz_tudo(file_name):
    pdf = convert_from_path('./files/' + file_name)
    folder_name = file_name.split('.')[0]
    os.mkdir(f'./files/images/{folder_name}')

    page_number = 0
    for page in pdf:
        page.save(f'./files/images/{folder_name}/{page_number}.png', 'PNG')
        page_number += 1

    shutil.rmtree(f'./files/images/{folder_name}')