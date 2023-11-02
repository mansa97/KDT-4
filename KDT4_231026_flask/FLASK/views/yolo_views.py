import io
import os
import json
from PIL import Image
import glob
import torch
from flask import Flask, jsonify, url_for, render_template, request, redirect, Blueprint,current_app


bp = Blueprint('yolo', __name__, url_prefix='/yolo')


RESULT_FOLDER = os.path.join('static')

@bp.record
def record_params(setup_state):
    app = setup_state.app
    app.config['RESULT_FOLDER'] = RESULT_FOLDER

# path = 'D:\EXAM_PANDAS\01_YOLO\basicflask\FLASK\FLSK_PJT\best.pt'
model = torch.hub.load(r'./static/yolov5-master', 'custom', path='./best.pt', source='local')

model.eval()

def get_prediction(img_bytes):
    img = Image.open(io.BytesIO(img_bytes))
    imgs = [img]  # batched list of images

# Inference
    results = model(imgs, size=640)  # includes NMS
    return results

@bp.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return render_template('yolo/index.html')

        img_bytes = file.read()
        results = get_prediction(img_bytes)       

        full_filename = os.path.join(current_app.config['RESULT_FOLDER'], 'results0.jpg')

        results.save(save_dir='static/result/')
        result_image='../static/result/image0.jpg'

        return redirect(result_image) #render_template('yolo/result.html',result_image=result_image) #'../static/result/image0.jpg'
    
    return render_template('yolo/index.html')

# @bp.route('/question')
# def main():
#     return redirect('/question/question_list')    
    