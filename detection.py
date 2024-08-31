import time
from collections import defaultdict
import utils
import threading
import multiprocessing

class Detection:
    def __init__(self, audio_processor, video_processor, cooldown_time=1):
        self.audio_processor = audio_processor
        self.video_processor = video_processor
        self.dice_roll_cache = defaultdict(int)
        self.summed_roll_cache = defaultdict(int)
        self.last_detected_time = 0
        self.cooldown_time = cooldown_time
        self.emp_fail = 0
        self.single_fail = 0
        self.multi_fail = 0

        # Initialize probabilities using utils.py
        self.probabilities = utils.initialize_probabilities()

        # Concurrency Control
        self.audio_detected_event = threading.Event()
        self.stop_event = threading.Event()

    def run_audio_detection(self):
        while not self.stop_event.is_set():
            if self.audio_processor.detect_specific_audio():
                self.audio_detected_event.set()

    def run_video_processing(self):
        while not self.stop_event.is_set():
            # Wait for audio detection signal
            self.audio_detected_event.wait()

            current_time = time.time()
            if current_time - self.last_detected_time < self.cooldown_time:
                self.audio_detected_event.clear()
                continue  # Skip if detection is within cooldown time

            image_path = self.video_processor.capture_screen_area()
            
            # Multiprocessing for image processing (optional)
            with multiprocessing.Pool(processes=1) as pool:
                labels = pool.apply(self.video_processor.detect_objects_in_image, args=(image_path,))

            if len(labels) == 0:
                self.emp_fail += 1
                print(f"Empty fail count: {self.emp_fail}")
                self.audio_detected_event.clear()
                continue
            elif len(labels) == 1:
                self.single_fail += 1
                print(f"Single fail count: {self.single_fail}")
                self.audio_detected_event.clear()
                continue
            elif len(labels) > 2:
                self.multi_fail += 1
                print(f"Multi fail count: {self.multi_fail}")
                self.audio_detected_event.clear()
                continue

            if len(labels) == 2:
                self.update_dice_roll_cache(labels)
                try:
                    dice_sum = sum(int(label) for label in labels)
                except ValueError:
                    print("Detected labels are not integers. Skipping this detection.")
                    self.audio_detected_event.clear()
                    continue

                if 2 <= dice_sum <= 12:
                    self.summed_roll_cache[dice_sum] += 1
                    total_rolls = sum(self.summed_roll_cache.values())
                    self.update_probabilities(total_rolls)
                    self.last_detected_time = current_time
                    self.plot_distributions()

            # Clear the event to wait for the next audio detection
            self.audio_detected_event.clear()

    def update_dice_roll_cache(self, labels):
        for label in labels:
            self.dice_roll_cache[label] += 1

    def update_probabilities(self, total_rolls):
        """
        Update the probability distribution based on the summed_roll_cache.
        Here, we calculate the relative frequency of each dice sum.
        """
        for roll_sum in range(2, 13):
            # To avoid division by zero, add a small epsilon
            self.probabilities[roll_sum] = (self.summed_roll_cache[roll_sum] + 1) / (total_rolls + 11)

    def plot_distributions(self):
        """
        Plot both the summed roll distribution and the probability distribution.
        """
        utils.plot_summed_distribution(self.summed_roll_cache)
        utils.plot_probability_distribution(self.probabilities)

    def start_detection(self):
        """
        Start the detection process with threading for concurrency.
        """
        audio_thread = threading.Thread(target=self.run_audio_detection)
        video_thread = threading.Thread(target=self.run_video_processing)

        audio_thread.start()
        video_thread.start()

        try:
            while audio_thread.is_alive() and video_thread.is_alive():
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.stop_event.set()
            print("Detection stopped by user.")

        audio_thread.join()
        video_thread.join()
