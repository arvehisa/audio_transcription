# Audio Transcription with AWS SageMaker

This project captures audio from a specified input device, processes it, and transcribes the audio using an AWS SageMaker Endpoint (Hosting Whisper). The transcriptions are saved to a text file.

## Features
- Real-time transcription every 10 seconds.

## Setup Instructions
To get started with this project, follow these steps:

1. **Specify the Audio Device Name**: Update the code with the name of your audio input device.
2. **Set the SageMaker Endpoint**: Define the `ENDPOINT_NAME` environment variable with your SageMaker Endpoint name.

## Prerequisites
Ensure you have the following installed and configured:

- **Python 3.x**
- **AWS CLI**: Configured with appropriate permissions.
- **Python Packages**:
  - `pyaudio`
  - `boto3`
  - `pydub`

