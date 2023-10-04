## Setup

### EC2 instance
`type = g4dn.xlarge`

### Login and setup

### Install CUDA

https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Debian&target_version=11&target_type=deb_network

### Run the following
`pip install virtualenv`

`virtualenv env`

`source env/bin/activate`

`pip install -r requirements.txt`

`sudo apt update && sudo apt install ffmpeg`

`jupyter notebook`

### Then open in chrome

http://localhost:8888/
