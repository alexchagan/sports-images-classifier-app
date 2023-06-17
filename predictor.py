from flask import Flask, request, redirect, render_template
from werkzeug.utils import  secure_filename
import os
from tensorflow import keras
import numpy as np
from utilities import load_image,get_classes


classes = get_classes()

app = Flask(__name__, static_url_path='/static')

app.config["IMAGE_UPLOADS"] = './static'
app.config["ALLOWED_IMAGE_EXTENSIONS"]=["JPEG", "JPG", "PNG"]

sport_prediction_model = keras.models.load_model('model/model.h5')

def allowed_image(filename):
    
    if not "." in filename: 
        return False
    
    ext = filename.rsplit(".", 1)[1] 

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


#  GET - approaching the sever without adding data
#  POST - adding data to the server like uploading images
@app.route("/", methods=["GET","POST"]) 
def upload_image() :
    
    if request.method == "POST": # verify if data coming to the server

        if request.files: # verify if a file is attached to the request 

            image = request.files["image"]

            if image.filename == "": # check if the image has empty file name

                return redirect(request.url) # stay in the same page and wait for another file to be uploaded

            if allowed_image(image.filename): # verify if the image has an allowed name

                filename = secure_filename(image.filename) # returns a secure version of the file
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                return redirect(f'/showing-image/{filename}')

            else:

                return redirect(request.url)
    
    # this part of the code is accesible if we are not using POST method

    return render_template("upload_images.html") # render_template automatically goes to the templates folder   


@app.route("/showing-image/<image_name>", methods=["GET","POST"])
def showing_image(image_name):

    if request.method == 'POST':

        if request.form["action"] == 'predict':
      
            image_path = os.path.join(app.config["IMAGE_UPLOADS"], image_name)
            image = load_image(path=image_path)
            image = np.expand_dims(image, axis=0)
            predictions = sport_prediction_model.predict(image)
            predicted_class_idx = np.argmax(predictions)
            probability = np.max(predictions)
            predicted_class = classes[predicted_class_idx]

            return render_template("prediction_result.html", image_name=image_name, predicted_class=predicted_class, probability=probability)
        
        if request.form["action"] == 'back':

            return redirect(f'/')

    return render_template("showing_image.html", value=image_name)



if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    # gunicorn -b 0.0.0.0:8080 predictor:app