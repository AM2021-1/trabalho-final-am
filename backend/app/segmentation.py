from pdf2image import convert_from_path
import os
import shutil

import detect

def parse_detection(xyxy):
    index = 0
    res = {}
    for item in xyxy:
        res[str(index)] = item.to_json(orient='records')

    return res

def faz_tudo(file_name, model):
    pdf = convert_from_path('./files/' + file_name)
    folder_name = file_name.split('.')[0]
    os.mkdir(f'./files/images/{folder_name}')

    page_number = 0
    for page in pdf:
        page.save(f'./files/images/{folder_name}/{page_number}.png', 'PNG')
        page_number += 1

    img = [f'./files/images/2021_10_21_ASSINADO_do2/{i}.png' for i in range(page_number)]

    results = model(img)

    # results.pandas().xyxy[0].to_json(orient="records")
    res = {}
    for i in range(len(img)):
        res[str(i+1)] = results.pandas().xyxy[i].to_json(orient='records')

    shutil.rmtree(f'./files/images/{folder_name}')

    return res
