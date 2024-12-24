# KidneyHealthPredictor
## Overview
KidneyHealthPredictor is a deep learning-based application designed to predict whether a kidney is healthy (normal) or affected by a tumor based on an uploaded image. The application utilizes a convolutional neural network (VGG16) model, trained on medical images, to accurately classify kidney health. This project aims to assist healthcare professionals by providing an AI-driven tool for early detection of kidney tumors, potentially enabling quicker intervention and improved patient outcomes.

The application allows users to upload kidney images (such as CT scans or X-rays), and it uses the trained deep learning model to predict whether the kidney is normal or affected by a tumor.

## Features
- **Image Upload**: Users can upload images of kidneys in formats such as JPG or PNG.
- **Prediction**: The app uses a pre-trained deep learning model to predict if the kidney is normal or has a tumor.
- **Result Display**: After prediction, the result is displayed to the user, showing whether the kidney is "Normal" or has a "Tumor".
- **Deep Learning Model**: The model is built using Convolutional Neural Networks (VGG16) to ensure high accuracy in image classification.

## 🛠️ Tech Stack
- **Backend**: Python, FastAPI(web framework for building APIs)
- **Frontend**: HTML, CSS, JavaScript (Interactive UI)
- **Deployment**: Docker,AWS(Cloud deployment)
- **MLOps Tools**: MLflow,DVC,Dagshub (A tools for managing the machine learning lifecycle and For managing large datasets)
- **Others**: Uvicorn, Jinja2 (ASGI server to run the FastAPI app and Templating engine used to render dynamic conten)

## How to Use
- **Upload Image**: On the main page, click the "Upload" button to choose a kidney image from your local machine.
- **Prediction**: Once the image is uploaded, the model will process it and display the result: either "Normal" or "Tumor".
- **Interpretation**: Based on the result, users can get insights into whether the kidney is healthy or potentially affected by a tumor.

## Installation Instructions
Follow these steps to set up the project locally:

Clone the repository

```bash
https://github.com/Srinath991/kidney-disease-clssification-app
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n ml python=3.8 -y
``` 
```bash
conda activate ml
```
### STEP 02- Set up the environment variables: Create a .env file in the project root with the following content:
    MLFLOW_TRACKING_PASSWORD= <mlflow_api_key>
    DAGSHUB_USERNAME=<dagshub_username>
    DAGSHUB_REPO=<dagshub_repo>

### STEP 03- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
uvicorn app.main:app --reload
```
Now,
open up you local host and port


## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)
- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

### DVC cmd
1. dvc init
2. dvc repro
3. dvc dag

## About MLflow & DVC
MLflow
 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model

DVC 
 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# AWS-CICD Deployment with GitHub Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

