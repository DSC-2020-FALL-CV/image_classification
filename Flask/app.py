import io
import json

import torch
from torch import nn
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request
from flask import render_template

import search

app = Flask(__name__)
# 여기서 주소를 자기가 저장한 곳으로
imagenet_class_index = json.load(open('./_static/dog_class_index.json'))
model = models.resnet18()
num_in = model.fc.in_features
num_out = 120
model.fc = nn.Sequential(
    nn.Linear(
        in_features = num_in,
        out_features = num_out,
        bias=True),
    nn.LogSoftmax(dim=1))
model.load_state_dict(torch.load('../Model/dog_prediction.pt', map_location=torch.device('cpu')))
model.eval()


def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        print(class_name)
        
        #delete _ and - from classname
        class_name = class_name.replace("_", " ")
        class_name = class_name.replace("-", " ")
        
        #search.wiki2(class_name)
        class_name, character, info, img_src = search.dogSite(class_name.replace(" ", "+"))

        return render_template('result.html', class_name=class_name, class_id=class_id, character = character, info = info, img_src = img_src)



if __name__ == '__main__':
    app.run(host='0.0.0.0')