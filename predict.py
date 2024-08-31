from ultralytics import YOLO

# Load the trained model
model = YOLO("best.pt")

# Predict on all images in the specified folder
model.predict(
    #source="D:\YOLOV8\predict",  # Replace with the path to your folder of images
    source=r"D:\YOLOV8\capture\current.png",  # Replace with the path to your folder of images
    show=True,
    save=True,
    #hide_labels=False,  # Ensure labels are shown
    #hide_conf=False,    # Ensure confidence scores are shown
    conf=0.6,           # Confidence threshold
    save_txt=False,     # Do not save labels in a text file
    save_crop=False,    # Do not save cropped predictions
    line_thickness=1,   # Thickness of bounding box lines
    visualize=False,
    verbose=True        # Verbose output for debugging
)
