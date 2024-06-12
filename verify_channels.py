import pyaudio

audio = pyaudio.PyAudio()

print("Available devices and their info:")
for i in range(audio.get_device_count()):
    info = audio.get_device_info_by_index(i)
    print(f"Device {info['index']}: {info['name']}, Channels: {info['maxInputChannels']}, Rate: {info['defaultSampleRate']}")