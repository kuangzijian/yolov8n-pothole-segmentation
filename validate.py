# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import glob
import os
from ultralyticsplus import YOLO, render_result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # load model
    model = YOLO("../runs/segment/train/weights/best.pt")
    model.task = 'segment'

    # start validation
    results = model.val(
        data="/dataset/data.yaml",
    )
