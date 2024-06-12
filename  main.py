import pyaudio
import boto3
import json
from pydub import AudioSegment
from io import BytesIO
from datetime import datetime
import os

# Function to find the device index by name and get max input channels and rate
def find_device_index_and_info(audio, name):
    device_count = audio.get_device_count()
    for i in range(device_count):
        device_info = audio.get_device_info_by_index(i)
        if name in device_info['name']:
            return i, device_info['maxInputChannels'], int(device_info['defaultSampleRate'])
    return None, None, None

# Initialize SageMaker client
client = boto3.client('runtime.sagemaker')
audio = pyaudio.PyAudio()
device_name = "Input" # Input your audio device name here

# Input the name of the transcript
transcript_name = input("Enter the name for the transcript: ")

# Find the index for the specified device and set channels and rate
device_index, CHANNELS, RATE = find_device_index_and_info(audio, device_name)
if device_index is None:
    raise Exception("Audio device not found")

# Set constants
FORMAT = pyaudio.paInt16
CHUNK = 4096
RECORD_SECONDS = 10
ENDPOINT_NAME = os.getenv('ENDPOINT_NAME')

# Open audio stream using the correct device index, channels, and rate 
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, input_device_index=device_index)

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = f"{current_time}_{transcript_name}.txt"

with open(file_path, "w") as f:
    try:
        print("start speaking...")
        while True:
            frames = [stream.read(CHUNK, exception_on_overflow=False) for _ in range(int(RATE / CHUNK * RECORD_SECONDS))]
            audio_segment = AudioSegment(data=b''.join(frames), sample_width=audio.get_sample_size(FORMAT), frame_rate=RATE, channels=CHANNELS)
            wav_io = BytesIO()
            audio_segment.export(wav_io, format="wav")
            response = client.invoke_endpoint(EndpointName=ENDPOINT_NAME, ContentType='audio/wav', Body=wav_io.getvalue())
            transcription = json.loads(response['Body'].read().decode())['text']
            print("Transcription:", transcription)
            f.write(" ".join(transcription) + "\n")
    except KeyboardInterrupt:
        print("Speaking ends.")
    finally:
        print(f"transcription saved: {file_path}")

# Clean up
stream.stop_stream()
stream.close()
audio.terminate()