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
1. **Supervised Learning**: The model learns from labeled data (input-output pairs).
Example: Predicting house prices (regression) or classifying emails as spam/not spam (classification).
Common algorithms: Linear regression, logistic regression, neural networks, random forests.
2. **Unsupervised Learning**: The model finds patterns in unlabeled data.
Example: Grouping customers by behavior (clustering) or reducing data dimensions (e.g., PCA).
Common algorithms: K-means clustering, hierarchical clustering, autoencoders.
3. **Reinforcement Learning**: The model learns by interacting with an environment, maximizing a reward.
Example: Training a robot to navigate obstacles or optimizing game strategies.
Common algorithms: Q-learning, deep Q-networks (DQN).


#### Applications
- **Daily Life**: Spam filters, recommendation systems (Netflix, Amazon), voice assistants.
- **Industry**: Fraud detection, medical diagnosis, predictive maintenance, autonomous vehicles.
- **Science**: Drug discovery, climate modeling, genomics.

### Supervised Learning (Labeled data, predicts outputs)
- **Linear Regression**: Predicts continuous values (e.g., house prices) by fitting a line to the data.
- **Logistic Regression**: Classifies binary outcomes (e.g., spam vs. not spam) using a sigmoid function.
- **Decision Trees**: Splits data into branches based on feature values for classification or regression.
- **Random Forest**: Ensemble of decision trees, reduces overfitting by averaging predictions.
- **Support Vector Machines (SVM)**: Finds a hyperplane to separate classes, effective for high-dimensional data.
- **Neural Networks**: Layers of interconnected nodes, great for complex tasks like image recognition.
- **Gradient Boosting (e.g., XGBoost, LightGBM)**: Builds trees sequentially, correcting errors of previous ones; strong for tabular data.
- 
### Unsupervised Learning (Unlabeled data, finds patterns)
- **K-Means Clustering**: Groups data into k clusters based on similarity.
- **Hierarchical Clustering**: Builds a tree of clusters, useful for nested structures.
- **Principal Component Analysis (PCA)**: Reduces dimensionality by projecting data onto principal components.
- **Autoencoders**: Neural networks for dimensionality reduction or anomaly detection.
  
### Reinforcement Learning (Learns through rewards)
- **Q-Learning**: Learns optimal actions by updating a value function based on rewards.
- **Deep Q-Networks (DQN)**: Combines Q-learning with neural networks for complex environments.
- **Policy Gradient Methods**: Directly optimizes actions for maximum reward (e.g., in robotics).

### Key Considerations
- **Choosing an Algorithm**: Depends on data size, feature types, task (classification, regression, clustering), and interpretability needs. For small datasets, simpler models like logistic regression or decision trees work well. For large, complex data, try neural networks or gradient boosting.
- **Evaluation Metrics**: Accuracy, precision, recall, F1-score (classification); RMSE, MAE (regression); silhouette score (clustering).
- **Tools**: Python libraries like scikit-learn, TensorFlow, PyTorch, or XGBoost are widely used.
