# Audio Transcription with AWS SageMaker

This project captures audio from a specified input device, processes it, and transcribes the audio using an AWS SageMaker Endpoint (Hosting Whisper). The transcriptions are saved to a text file.

## Features
- Real-time transcription every 10 seconds.

## Setup Instructions
To get started with this project, follow these steps:

1. Specify the audio device name
2. Specify your sagemaker endpoin name

## Prerequisites
Ensure you have the following installed and configured:

- **AWS CLI**: Configured with appropriate permissions.
- **Python Packages**:
  - `pyaudio`
  - `boto3`
  - `pydub`

## Relative Blog
https://zenn.dev/zhizhiarv/articles/whisper-realtime-transcribe-macbook

