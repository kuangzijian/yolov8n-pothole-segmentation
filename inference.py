# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import glob
import os
from ultralyticsplus import YOLO, render_result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # load model
    model = YOLO('runs/segment/train7/weights/best.pt')

    # set model parameters
    model.overrides['conf'] = 0.25  # NMS confidence threshold
    model.overrides['iou'] = 0.45  # NMS IoU threshold
    model.overrides['agnostic_nms'] = False  # NMS class-agnostic
    model.overrides['max_det'] = 1000  # maximum number of detections per image

    # load images
    filePath = 'dataset/inference'

    # Get a list of all files in the directory
    file_list = glob.glob(os.path.join(filePath, '*'))

    # Loop through each file
    for image in file_list:
        file_name = os.path.basename(image)
        print("Predict result for image: " + file_name)

        # perform inference
        results = model.predict(image)

        # observe results
        print(results[0].boxes)
        print(results[0].masks)
        render = render_result(model=model, image=image, result=results[0])
        render.save('dataset/inference_result/' + file_name, 'png')
        #render.show()
