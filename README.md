# DS5110 Final Project

## Team members:
* Dominic Dill
* Casey Tilton
* Alexey Rizvanov

## Goal
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Institute for Experiential AI is working with the Northeastern University Library to help categorize thousands of recently digitized historical images from Boston Globe archives. Most of these images lack metadata, and there is an inconsistent format for the few that do. The goal of this project is to utilize data science techniques to aid in the tagging of these images, enabling the public to easily search through these historical photos with relevant keywords.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Alexey, Casey, and Dominic have each attempted to automate the tagging of these images through the use of pre trained models. Fast AI, Google Vision, and DeepFace were the tools of choice, and a brief description of the outcome can be found below.

## #1 - Fast AI - Casey
to do - intro to your part
## #2 - Google Vision - Alexey
to do - intro to your part
## #3 - DeepFace - Dominic
First, you need to install deepface:

```$ pip install deepface```

Tensorflow is a dependency, so if you don't have it, it will most likely be pulled in as well.


Below description is from [Deepface's GitHub page](https://github.com/serengil/deepface):
> Deepface is a lightweight [face recognition](https://sefiks.com/2018/08/06/deep-face-recognition-with-keras/) and facial attribute analysis 
([age](https://sefiks.com/2019/02/13/apparent-age-and-gender-prediction-in-keras/), [gender](https://sefiks.com/2019/02/13/apparent-age-and-gender-prediction-in-keras/), [emotion](https://sefiks.com/2018/01/01/facial-expression-recognition-with-keras/) and [race](https://sefiks.com/2019/11/11/race-and-ethnicity-prediction-in-keras/)) 
framework for python. It is a hybrid face recognition framework wrapping **state-of-the-art** models: [`VGG-Face`](https://sefiks.com/2018/08/06/deep-face-recognition-with-keras/), [`Google FaceNet`](https://sefiks.com/2018/09/03/face-recognition-with-facenet-in-keras/), [`OpenFace`](https://sefiks.com/2019/07/21/face-recognition-with-openface-in-keras/), [`Facebook DeepFace`](https://sefiks.com/2020/02/17/face-recognition-with-facebook-deepface-in-keras/), [`DeepID`](https://sefiks.com/2020/06/16/face-recognition-with-deepid-in-keras/), [`ArcFace`](https://sefiks.com/2020/12/14/deep-face-recognition-with-arcface-in-keras-and-python/), [`Dlib`](https://sefiks.com/2020/07/11/face-recognition-with-dlib-in-python/) and `SFace`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The default DeepFace settings (which utilizes openCV's pre trained [haar-cascade](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) face detection algorithm) have been used to count faces in images. While the process is not perfect, it may be a useful tool for distinguishing between images with and without faces. When executed, the `/src/deepface/SearchFunctions/countfaces.py` script will search image files placed in the `/data/all_images/`
for faces. It will then create a `.csv` file with the face counts for each image and store it in the `/data/deepface/deepface_tags/face_counts/` folder. This file could then be used as a filter for downstream classifiers, sending images with no detected faces to models trained for landscape and object detection, and images with detected faces to models designed for facial recognition.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Facial detection is computationally expensive. Initial testing with images from the dataset, which are very high resolution and on the order of 100mb to 300mb, shows that detection times can range from 100s of milliseconds to 10+ seconds per image. OpenCV's haar-cascade algorithm is comparatively quick, but the speed comes with a decrease in the ability to correctly detect faces. [For comparison](https://sefiks.com/2020/08/25/deep-face-detection-with-opencv-in-python/), the ssd method is faster, but even worse at detecting faces, while the mtcnn method is slower, but more accurate. For a more detailed inspection of this, refer to `/src/deepface/DemoNotebooks/FaceDetectorDemoWithBoxes.ipynb`  


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Facial detection is only the first step in the 4 step process that is known as facial recognition. Recognition requires not only facial detection, but identification. To accomplish this, known faces are usually stored as vector representations, and then compared against the vector representation of a detected face. If the difference between the two is below a certain threshold, then the detected face becomes recognized. DeepFace's `DeepFace.find()` allows for this to be accomplished with only a few lines of code. The default functionality utilizes the pre-trained openCV haar-cascade and VGG-Face models and cosine similarity to assess vector differences. An example of this can be found in the `/src/deepface/SearchFunctions/facesearch.py` script, which will search through the image files placed in `/data/all_images/` and check them against images of known faces in the `/data/deepface_known_faces/`. A `.csv` file will then be created associating images of unknown faces with the images of known faces.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Future prospects: Through the use of facial recognition, we are able to use any facial image as a query for images containing similar faces. In this case, we could quickly identify images that possibly contain faces of any known perosn, as long as we have a facial image of that person. For example, if all of the photos from this dataset were run through a facial recognition pipeline, then it would be possible to use facial images from outside the dataset to identify images within the dataset that contain similar faces. For more information, see [Deep Face Recognition with Relational Databases and SQL](https://sefiks.com/2021/02/06/deep-face-recognition-with-sql/).


