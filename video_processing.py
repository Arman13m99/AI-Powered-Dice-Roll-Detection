import mss
import cv2
import numpy as np
from ultralytics import YOLO

class VideoProcessor:
    def __init__(self, model_path, monitor):
        self.yolo_model = YOLO(model_path)
        self.monitor = monitor

    def capture_screen_area(self):
        """ Capture the screen area and save the image. """
        with mss.mss() as sct:
            screen = np.array(sct.grab(self.monitor))
            img_bgr = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)
            img_path = "D:/My Project 01/capture/current.png"
            cv2.imwrite(img_path, img_bgr)
            return img_path

    def detect_objects_in_image(self, image_path):
        """ Detect objects in the image and return labels. """
        results = self.yolo_model.predict(
            source=image_path,
            show=False,
            save=False,
            conf=0.6,
            save_txt=False,
            save_crop=False,
            line_thickness=1,
            verbose=False
        )
        for result in results:
            labels = [self.yolo_model.names[int(cls)] for cls in result.boxes.cls]
            return labels
