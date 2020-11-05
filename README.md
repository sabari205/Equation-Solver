# Handwritten Equation solver

The application will be able to predict and solve handwritten mathematical equations from the given image. The system should be capable of solving expression involving arithmetic operations (addition, subtraction, multiplication, division) and solve equations of any degree (linear, quadratic, cubic and so on).

Key AI concepts used include OCR (Optical Character Recognition) and CNN (Convolutional Neural Networks). OCR is used to preprocess the image and segment characters, while CNN is used to predict the characters.

Download the repo, move to the folder and run

## Installation

The repository can either be cloned or downloaded as a zip.

Run `npm install` inside the project directory to install all dependencies.

## Execution

Both ReactJS and Flask have to be executed :

```
npm start
cd Equation-Solver
python -m flask run
```

## Result 

### When image is written through sketchpad


<p float="left" align="middle">
   <img src="https://github.com/sabari205/Equation-solver/blob/master/images/sketchpad1.jpeg" alt="sketchpad-1" width="500" />
    <img src="https://github.com/sabari205/Equation-solver/blob/master/images/sketchpad2.jpeg" alt="sketchpad-2" width="500" /> 
</p>



### When image is uploaded


<p float="left" align="middle">
   <img src="https://github.com/sabari205/Equation-solver/blob/master/images/uploaded1.png" alt="uploaded-1" width="500" />
    <img src="https://github.com/sabari205/Equation-solver/blob/master/images/uploaded2.png" alt="uploaded-2" width="500" /> 
</p>


## Overview

<img src="https://github.com/sabari205/Equation-solver/blob/master/images/architecture.png" alt="Architecture" height = "600" width = "600">

- The [**Frontend**](https://github.com/sabari205/Equation-Solver/tree/master/src) part has been developed using `ReactJS`. Here the user enters the image either by uploading or by using the sketchpad. The image is encoded to base64 format and sent to the REST-API as a POST request.

- The [**REST-API**](https://github.com/sabari205/Equation-Solver/blob/master/Equation-Solver-main/app.py) has been implemented using `Flask`. The request data is decoded and saved as an image locally and this image is sent to the backend where the equation is predicted and solved.

- The [**Backend**](https://github.com/sabari205/Equation-Solver/tree/master/Equation-Solver-main) has been implemented using `Python, Tensorflow and OpenCV`. The backend can be seen as two separate modules : Equation Prediction and Equation Solver.
    
    - OpenCV is used to perform binarization and line and character segmentation. A Tensorflow model trained using the EMNIST (Extended MNIST) dataset is used to predict each of the segmented characters and the equation generated is passed as a string to the Equation Solver.
    
    - The Equation Solver solves the mathematical equation and passes it back to the Frontend where it can be viewed.

## Character Segmentation

The major steps include : Noise Removal, Binarization, Thresholding and Image Segmentation.

The Binarized image and the segmented images can be viewed below :

<img src="https://github.com/sabari205/Equation-solver/blob/master/images/char-segmentation.png" alt="Architecture" height = "600" width = "600">

## Solving the Equation

After each of the character in the image is detected, the string containing the equation is passed to this final module which solves the equation or mathematical expression.

The equation can be of two types :

- A mathematical string such as ‘5+3’ or ‘66x3+2’ (String that is input to this module is of this format). This string can either be evaluated using a custom-built function or the eval( ) function in python.

- A mathematical equation of any degree. The string ‘X2+5=0’ is interpreted as `X**2 + 5` since the 2 appears after the variable. Whereas `2X+5=0` is interpreted as 2*X + 5 = 0. Since prediction of even a single character leads to incorrect results/failure, simple replacements are performed on the given string to increase accuracy. These include Z -> 2, G -> 6, B -> 8 and D -> 0. The equation is solved using the SymPy library, which is a python library for symbolic computation.

The 2 types of equations are distinguished by checking if the equation contains ‘=‘. If the equation contains ‘=‘, it is interpreted as the 2nd type, otherwise it is interpreted as the 1st type.

## Links 

[Link to the presentation](https://drive.google.com/file/d/1f7ZVFmpK5mBtrZ68hBml8bGoJ_VRc_ih/view?usp=sharing)

## References 

[Introduction to CNN Keras](https://www.kaggle.com/yassineghouzam/introduction-to-cnn-keras-0-997-top-6)

[Character Segmentation](https://github.com/dishank-b/Character_Segmentation)

[ReactJS - Getting Started](https://reactjs.org/docs/getting-started.html)

[React - P5 Wrapper](https://github.com/and-who/react-p5-wrapper)

[Flask Restful](https://flask-restful.readthedocs.io/)

[React bootstrap](https://react-bootstrap.github.io/)

