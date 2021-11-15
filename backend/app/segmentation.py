from pdf2image import convert_from_path
import os
import shutil
import pytesseract
import json
import cv2
import math
import pandas

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

    img = [f'./files/images/{folder_name}/{i}.png' for i in range(page_number)]

    results = model(img)

    print('RESULTS: '+ str(len(results)))

    res = {}
    for i in range(len(img)):
        aux = json.loads(results.pandas().xyxy[i].to_json(orient='records'))
        text = []
        image = cv2.imread(f'./files/images/{folder_name}/{i}.png', 0)
        thresh = 255 - cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        j = 0
        for bbox in aux:
            print(f'On IMG: {i} - Bbox: {j}')

            x,y,w,h = math.floor(bbox['xmin']), math.floor(bbox['ymin']), math.floor(bbox['xmax']), math.floor(bbox['ymax'])

            ROI = thresh[y:y+h,x:x+w]
            data = pytesseract.image_to_string(ROI, lang='eng',config='--psm 6')

            text.append({ 'text': data, 'label': bbox['name'] })
            j+=1
        res[str(i+1)] = text


    shutil.rmtree(f'./files/images/{folder_name}')

    return res
