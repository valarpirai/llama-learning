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

## Machine Learning
Machine learning (ML) is a subset of artificial intelligence where computers learn patterns from data to make predictions or decisions without being explicitly programmed. Instead of following fixed rules, ML algorithms improve their performance as they process more data.

#### Core Concepts
- Data: ML relies on data (e.g., numbers, images, text) to train models. More diverse, high-quality data leads to better models.
- Models: Algorithms that learn patterns from data (e.g., decision trees, neural networks).
- Training: The process of feeding data to a model so it can adjust its internal parameters to minimize errors.
- Prediction/Inference: Using a trained model to make predictions on new, unseen data.

#### Types of Machine Learning
1. Supervised Learning: The model learns from labeled data (input-output pairs).
Example: Predicting house prices (regression) or classifying emails as spam/not spam (classification).
Common algorithms: Linear regression, logistic regression, neural networks, random forests.
2. Unsupervised Learning: The model finds patterns in unlabeled data.
Example: Grouping customers by behavior (clustering) or reducing data dimensions (e.g., PCA).
Common algorithms: K-means clustering, hierarchical clustering, autoencoders.
3. Reinforcement Learning: The model learns by interacting with an environment, maximizing a reward.
Example: Training a robot to navigate obstacles or optimizing game strategies.
Common algorithms: Q-learning, deep Q-networks (DQN).
