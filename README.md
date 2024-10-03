## Setup

### EC2 instance
`type = g4dn.xlarge`

### Login and setup

### Install CUDA

https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Debian&target_version=11&target_type=deb_network

## Setup 
Run the following command to setup
`./bin/setup.sh`

Install the following tools in Linux

`sudo apt update && sudo apt install ffmpeg`

For Mac

`brew install ffmpeg`

Download OpenAI Whisper Models

`./download_whisper_models.sh`

Run the command to start notebook server

`source learning-env/bin/activate`

`jupyter notebook`

### Then open in chrome

http://localhost:8888/
