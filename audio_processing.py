import pyaudio
import numpy as np
import tensorflow as tf

# Constants for audio processing
SAMPLE_RATE = 16000
CHUNK_SIZE = 13000
FRAME_LENGTH = 500
FRAME_STEP = 128

class AudioProcessor:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=SAMPLE_RATE, input=True, frames_per_buffer=CHUNK_SIZE)

    def preprocess_audio(self, audio_chunk):
        """ Preprocess the audio chunk for model prediction. """
        audio_chunk = np.frombuffer(audio_chunk, dtype=np.int16).astype(np.float32)
        audio_chunk = audio_chunk / np.max(np.abs(audio_chunk))  # Normalize

        wav_tensor = tf.convert_to_tensor(audio_chunk, dtype=tf.float32)
        wav_tensor = wav_tensor[:CHUNK_SIZE]
        zero_padding = tf.zeros([CHUNK_SIZE] - tf.shape(wav_tensor), dtype=tf.float32)
        wav_tensor = tf.concat([zero_padding, wav_tensor], 0)

        spectrogram = tf.signal.stft(wav_tensor, frame_length=FRAME_LENGTH, frame_step=FRAME_STEP)
        spectrogram = tf.abs(spectrogram)
        spectrogram = tf.expand_dims(spectrogram, axis=2)

        return spectrogram

    def detect_specific_audio(self):
        """ Function to detect if a specific audio (like a dice roll) is played. """
        try:
            audio_chunk = self.stream.read(CHUNK_SIZE)
            spectrogram = self.preprocess_audio(audio_chunk)
            spectrogram = tf.expand_dims(spectrogram, axis=0)  # Add batch dimension
            prediction = self.model.predict(spectrogram)
            return prediction[0][0] > 0.9
        except Exception as e:
            print(f"An error occurred in audio detection: {e}")
            return False

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
