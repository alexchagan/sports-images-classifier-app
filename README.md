

[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
 
  <h3 align="center">Sports Images Classifier Application</h3>
 
</div>



<!-- ABOUT THE PROJECT -->
## About The Project

This is an application built to demonstrate the capabilities of a CNN model, trained on images of different genres of sports.
The user can upload an image of choise from the local dierctory and test the model.
The process of training and testing the model is documented in my other repository: https://github.com/alexchagan/sports-images-classifier

A google cloud deployed version of this application can be found here: https://sports-classifier-app-7m5cozwema-uc.a.run.app


![alt text](https://i.ibb.co/zhndbmN/homepage.png)

![alt text](https://i.ibb.co/PWggBXX/prediction.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Flask][Flask.js]][TensorFlow-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation


1. Clone the repo
   ```
   git clone https://github.com/alexchagan/sports-images-classifier-app.git
   ```
2. Install requirements
   ```
   pip install -r requirements
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* The google cloud application can be reached by the following link: https://sports-classifier-app-7m5cozwema-uc.a.run.app
 
* Can run the application locally by using command: 
  ```
   gunicorn -b 0.0.0.0:8080 predictor:app
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
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[Flask.js]: https://img.shields.io/badge/-Flask-black

