# Bangalore Travel Time Estimator

## Project Overview

The **Bangalore Travel Time Estimator** is a web application that allows users to predict travel times between two locations within the city of Bangalore, India. This application leverages a machine learning model to provide accurate travel time predictions based on geographical coordinates. Users can input the latitude and longitude of their source and destination, and the model will estimate the travel time.

## Table of Contents

- [Features](#features)
- [Machine Learning Model](#machine-learning-model)
- [Data Source](#data-source)
- [Model Training](#model-training)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Containerization](#docker-containerization)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Travel Time Prediction**: Input geographical coordinates (latitude and longitude) for the source and destination, and the application predicts the travel time.

## Machine Learning Model

The application utilizes an XGBoost-based machine learning model to make travel time predictions. This model was trained on historical trip data and incorporates features such as source and destination coordinates, hour of the day, and geodesic distance between the locations.

### Data Source

The dataset used for model training was obtained from Uber Movement and consisted of historical trip data within Bangalore city. Each quarterly dataset included columns like source ID, destination ID (assigned to each ward in the city), hour of the day, and mean travel time. Additionally, a geojson file containing the ward boundaries of the city was used.

### Model Training

The model was developed through the following steps:

1. **Feature Engineering**: Rigorous feature engineering was performed on the historical trip data, resulting in a dataset containing features like 'Source Latitude,' 'Source Longitude,' 'Destination Latitude,' 'Destination Longitude,' 'Hour of Day,' and 'Geodesic Distance.' The target variable was 'Mean Travel Time.'

2. **XGBoost Algorithm**: The XGBoost algorithm was employed to train the model. It achieved a high R-squared (R2) score, indicating its accuracy.

3. **Validation**: To validate the model, travel time predictions were compared to those from Google Maps for the same source and destination. The model closely matched Google Maps' estimates, differing by only a few minutes.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/sharan1133/Travel-Time-Estimator.git

## Usage

**Build and Run the Docker Container**

To build and run the Docker container, use the following commands:

1. Build the Docker image:

```bash
      docker build -t bangalore-travel-time-app .

      docker run -d -p 5000:5000 --name bangalore-travel-time-app bangalore-travel-time-app

After running the container, access the URL "[http://127.0.0.1:5000/](http://127.0.0.1:5000/)" on your browser to use the application.

      
