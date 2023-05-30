# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import glob
import os
from ultralyticsplus import YOLO, render_result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # load model
    model = YOLO("yolov8n-seg.pt")
    model.task='segment'
    # start training
    results = model.train(
        batch=8,
        device="cpu",
        data="dataset/train/data.yaml",
        epochs=7,
        imgsz=120,
    )