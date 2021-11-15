import torch
import pandas

# Model
model = torch.hub.load('/home/tiveron/faculdade/AM/a/trabalho-final-am/backend/yolov5', 'custom', path='./best.pt', source='local')  # or yolov5m, yolov5l, yolov5x, custom

# Images
img = [f'./files/images/2021_10_21_ASSINADO_do2/{i}.png' for i in range(46)]  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
# results.print()
print(results.pandas().xyxy)
