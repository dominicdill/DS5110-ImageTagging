# Plan

* Goals

The Institute for Experiental AI is f

* Data
  * Description of the dataset.
  * Include any data-accessibility issues encountered or anticipated.
* Stakeholder feedback 
  * Briefly describe any feedback that you have received so far from your stakeholder.
  * If you have yet to meet with your stakeholder, then provide a date by which you'll expect to meet with them.
* EDA
  * One or more figures demonstrating exploratory analysis of the data.
  * Present results following the format of https://github.com/ds5110/git-intro
  * In particular, the repo's README.md should include instructions for reproducibility
* Timeline
  * Milestones for completion of the project
  * This should include at least one meeting with your stakeholder to review progress and get feedback.

March 27 - stakeholder kickoff meeting
March 28 - April 17 - group members will research their respective pre-trained image classification models and arrive at an initial set of findings
April 14-17 - group will meet during this period to discuss progress and put together presentation
April 18 - project presentation on Tuesday night
April 19 - 25 – if necessary, continue researching and refining models, and finalize project repo and front-facing HTML page for submission
April 25 - submit project materials

* Roles & responsibilities
  * Briefly describe (list of activities) the way that you've broken down individual contributions by team member.
  * Include plans for a front-facing HTML page or markdown file that presents results concisely for your stakeholder.
    * The front-facing page should be readable by a non-technical audience.
    * Note: put this front-facing page in the `/docs` directory
* Issues
  * Deacribe any and all obstacles/risks/challenges, encountered so far and/or anticipated

There have been numerous challenges so far that have indirectly and directly led to changes in the goals and scope of the project.

The original image dataset shared with us consists of very low resolution photos. Relatedly, the metadata for this dataset in the form of xml files are messy and inconsistent. This likely won’t matter in the end, as we now have access to higher resolution versions of the small subset of images that we will work with. 

Perhaps most importantly, we aren’t trained yet in deep learning/computer vision and any other techniques necessary to fully understand how to use image classification machine learning models. Our success in this project relies on our ability to use pre-trained models as black boxes. If the project continues beyond the end of the semester, we would have more time to learn how to control hyperparameters to improve classification results. 

An open question is about how we are supposed to empirically compare results of different models if we don’t have any training data. The best we can do is to output predictions for small subsets of images at a time using pre-trained models, then compare the predictions for each image across the models. But without labeled training data, we will be unable to do anything to tweak the results of the various models or even have the model calculate its own accuracy score. 
