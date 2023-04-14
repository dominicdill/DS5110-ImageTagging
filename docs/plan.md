# Plan

## Goals

This project aims to compare the image classifying capabilities of pre trained models using a collection of images from the Boston Globe and NEU library. Of the available pre trained mdoels, we have decided to work on implementing VGG16, FastAI, Google Vision and DeepFace for this project. There will be little, if any, training on the Boston Globe data set. We aim to compare the "out-of-the-box" capabilities of these pre trained models. A small subset of photos that have been previously run through AWS Rekognition by another team will be used as a form of accuracy / comparison check.

## Data
  * Description of the dataset.
  * Include any data-accessibility issues encountered or anticipated.

The dataset is a collection of high resolution, digitized photos from Boston Globe collection that the NEU library is working on making publicly accessible. A subset of this dataset has metadata associated with it. Unfortunately, there isn't a collection of these images with metadata that is easily accessible to us. Additionaly, the very high resolution of these images leads to large file sizes, which makes it difficult for personal computers to assess large groups of them quickly. Because of these issues, we will be working with a small subset (~100) of the images (and images only, no metadata). We will use this subset to manually check the validity of the tags produced by the pre trained models. 
 
## Stakeholder feedback 
  * Briefly describe any feedback that you have received so far from your stakeholder.
  * If you have yet to meet with your stakeholder, then provide a date by which you'll expect to meet with them.

We met with Guilia Taurino, our primary point of contact and stakeholder with the Institute of Experiential AI, on March 27 to discuss the goals for this process. After our initial meeting, we have further honed the focus of our project through email communication. As of April 4, the plan is for Guilia to send a list of images that have been previously run through AWS Rekognition so that we can compare results from our research on the same set of images. 

## EDA
  * One or more figures demonstrating exploratory analysis of the data.
  * Present results following the format of https://github.com/ds5110/git-intro
  * In particular, the repo's README.md should include instructions for reproducibility

As of April 4, we are waiting for a list of images that have already been run through AWS Rekognition. Once we have those images, we can report various descriptive statistics for the image files.
  * descriptive statistics of the file sizes (average, range, median, mode, etc)
  * Are all the photos black and white or are some in color?
  * AWS Rekognition output data


## Timeline

* March 27 - stakeholder kickoff meeting
* March 28 - April 17 - group members will research their respective pre-trained image classification models and arrive at an initial set of findings
* April 14-17 - group will meet during this period to discuss progress and put together presentation
* April 18 - project presentation on Tuesday night
* April 19 - 25 – if necessary, continue researching and refining models, and finalize project repo and front-facing HTML page for submission
* April 25 - submit project materials

## Roles & responsibilities
  * Briefly describe (list of activities) the way that you've broken down individual contributions by team member.
  * Include plans for a front-facing HTML page or markdown file that presents results concisely for your stakeholder.
    * The front-facing page should be readable by a non-technical audience.
    * Note: put this front-facing page in the `/docs` directory

### Dom
Research the viability of VGG16 and DeepFace model

### Casey 
Research the CNN model through fastai python library

### Alex
Research Google vision and Facebook deepface


## Issues
  * Deacribe any and all obstacles/risks/challenges, encountered so far and/or anticipated

There have been numerous challenges so far that have indirectly and directly led to changes in the goals and scope of the project.

The original image dataset shared with us consists of very low resolution photos. Relatedly, the metadata for this dataset in the form of xml files are messy and inconsistent. This likely won’t matter in the end, as we now have access to higher resolution versions of the small subset of images that we will work with. 

Perhaps most importantly, we aren’t trained yet in deep learning/computer vision and any other techniques necessary to fully understand how to use image classification machine learning models. Our success in this project relies on our ability to use pre-trained models as black boxes. If the project continues beyond the end of the semester, we would have more time to learn how to control hyperparameters to improve classification results. 

An open question is about how we are supposed to empirically compare results of different models if we don’t have any training data. The best we can do is to output predictions for small subsets of images at a time using pre-trained models, then compare the predictions for each image across the models. But without labeled training data, we will be unable to do anything to tweak the results of the various models or even have the model calculate its own accuracy score. 