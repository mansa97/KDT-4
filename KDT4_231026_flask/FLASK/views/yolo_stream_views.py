from flask import Flask, Response
import cv2
import torch
from flask import Blueprint, request, render_template, redirect

bp = Blueprint('yolo_stream', __name__, url_prefix='/stream')

# YOLOv5 모델 로드
model = torch.hub.load(r'./static/yolov5-master', 'custom', path = './best.pt', source='local')

model.eval()

# 카메라 스트림을 읽기 위한 함수
def generate_frames():
    # 카메라 설정 (0: 기본 카메라)
    cap = cv2.VideoCapture(0)
    # cap = cv2.flip(cap,1)


    while True:
        # 프레임 읽기
        success, frame = cap.read()
        if not success:
            break
        frame_flip = cv2.flip(frame, 1)
        # YOLOv5 모델로 객체 감지 수행
        results = model([frame_flip])  # 모델에 프레임 전달
        
        processed_frame = results.render()[0]  # 객체 감지 결과 렌더링된 프레임
        
        # 렌더링된 프레임을 웹 페이지로 스트리밍
        ret, buffer = cv2.imencode('.jpg', processed_frame)

        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # 웹 페이지로 프레임 전송

@bp.route('/')
def index():
    # HTTP response를 스트리밍으로 반환
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')