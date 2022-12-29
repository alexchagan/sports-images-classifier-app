

[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
 
  <h3 align="center">Sports Image Classifier Application</h3>
 
</div>



<!-- ABOUT THE PROJECT -->
## About The Project

This is an application built to demonstrate the capabilities of a CNN model, trained on images of different genres of sports.
The user can upload an image of choise from the local dierctory and test the model.
The process of training and testing the model is documented in my other repository: https://github.com/alexchagan/sports-images-classifier

A google cloud deployed version of this application can be found here: 


![alt text](https://i.ibb.co/zhndbmN/homepage.png)

![alt text](https://i.ibb.co/PWggBXX/prediction.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![TensorFlow][TensorFlow.js]][TensorFlow-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Download the kaggle dataset from: https://www.kaggle.com/datasets/gpiosenka/sports-classification/download?datasetVersionNumber=8 
 

### Installation


1. Clone the repo
   ```
   git clone https://https://github.com/alexchagan/sports-images-classifier.git
   ```
2. Install requirements
   ```
   pip install -r requirements
   ```
3. Place the train,val,test folders you downloaded from kaggle into sports-classifier-data folder 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. You can train your own model on the kaggle data or your own data with:
  ```
   python trainer.py
  ```

2. You can test your model on the test data with:
  ```
   python inference.py
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Alex Chagan  - alexchagan95@gmail.com

Project Link: [https://github.com/alexchagan/sports-images-classifier](https://github.com/alexchagan/sports-images-classifier)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alex-chagan-a243221b6/
[TensorFlow-url]: https://www.tensorflow.org/
[TensorFlow.js]: https://data.apkbe.com/5d/cc.nextlabs.tensorflow/1.0.3/icon.png!s

