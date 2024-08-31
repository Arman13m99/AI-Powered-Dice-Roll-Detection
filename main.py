from audio_processing import AudioProcessor
from video_processing import VideoProcessor
from detection import Detection
import utils  # If needed elsewhere in main.py

if __name__ == "__main__":
    # Initialize AudioProcessor and VideoProcessor with appropriate model paths and monitor settings
    audio_processor = AudioProcessor(model_path=r"D:\My Project 01\tf.io3-first-try3.h5")
    video_processor = VideoProcessor(
        model_path=r"D:\My Project 01\best.pt",
        monitor={"top": 700, "left": 1700, "width": 640, "height": 640}
    )

    # Initialize Detection with the processors
    detection = Detection(audio_processor, video_processor)

    # Start the detection process
    detection.start_detection()
