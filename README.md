# Handwritten Equation solver

The application will be able to predict and solve handwritten mathematical equations from the given image. The system should be capable of solving expression involving arithmetic operations (addition, subtraction, multiplication, division) and solve equations of any degree (linear, quadratic, cubic and so on).

Key AI concepts used include OCR (Optical Character Recognition) and CNN (Convolutional Neural Networks). OCR is used to preprocess the image and segment characters, while CNN is used to predict the characters.

Download the repo, move to the folder and run

## Installation

The repository can either be cloned or downloaded as a zip.

Run `npm install` inside the project directory to install all dependencies.

## Overview

<img src="https://github.com/sabari205/Equation-solver/blob/master/images/architecture.png" alt="Architecture" >

- The Frontend part has been developed using ReactJS. Here the user enters the image either by uploading or by using the sketchpad. The image is encoded to base64 format and sent to the REST-API as a POST request.

- The REST-API has been implemented using Flask. The request data is decoded and saved as an image locally and this image is sent to the backend where the equation is predicted and solved.

- The Backend has been implemented using Python, Tensorflow and OpenCV. The backend can be seen as two separate modules : Equation Prediction and Equation Solver.
    
    - OpenCV is used to perform binarization and line and character segmentation. A Tensorflow model trained using the EMNIST (Extended MNIST) dataset is used to predict each of the segmented characters and the equation generated is passed as a string to the Equation Solver.
    
    - The Equation Solver solves the mathematical equation and passes it back to the Frontend where it can be viewed.


# Running the app

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.
