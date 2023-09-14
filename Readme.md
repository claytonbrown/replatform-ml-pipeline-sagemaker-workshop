                                        Welcome to the replatforming ML pipeline workshop. 

Hi There,

Welcome to this Workshop for replatforming ML pipeline to Sagemaker Pipelines

Github - https://github.com/sumirk/replatform-ml-pipeline-sagemaker-workshop/tree/main

The Fashion MNIST dataset is a well-known dataset in the field of machine learning and computer vision. It consists of grayscale images of clothing items, each belonging to one of ten classes, including items like T-shirts, dresses, sneakers, and more.

The example here is a multi-class image classification problem. The goal was to build and train a deep learning model that could correctly classify these clothing items into their respective classes based on the images.

Please note that is a simplified example for illustration purposes


Setting expectations:-

     - This is not a Machine learning workshop but rather a Machine learning engineering workshop.
     - You do not need to know ML algorithms but just enough knowledge to understand the process and the important steps.
     - You will have to go through a lot of Python code re-structuring, Sagemaker concepts etc.
     - However, if you stay put you will have a very practical understanding of what it takes to work with customers on their ML engineering projects.
     - This is just scratching the surface, the actual projects still go very far, but if you are able to do this believe me a lot of customers still have a very manual and legacy ML engineering practices.


The goal of the workshop is to modularize the existing ML pipeline which was running on ECS Fargate task with below outcomes:-

     - Each individual task can be scaled individually and the pipeline can be resumed from the failed task.
     - The intermediate files and atrifacts should be available on S3
     - Optional - Run local testing in local mode on compute outside of Sagemaker managed environments.
     - Using minimum operations and without building custom docker containers for SageMaker.
     - Ability to re-run the re-training pipeline and have the artifacts in an organized way per run for all the tasks.
     - Handle the checkpoints and ability to resume from the failed training job from the last checkpoint.
     - Push the training metrics from model training script to Sagemaker Experiments. Visualize the training metrics to understand loss and accuracy over checkpoints.
     - Register the model with the model metrics converted to Sagemaker model metrics format.
     - Passing custom metadata to add any additional pipeline context like pipeline-run-id or maybe input parameters, hyperparameters etc to the registered model to compare models easily.



- Create a S3bucket in your account

- If you do not have a Sagemaker Studio and a Cloud9 environment then use the below CFN template to deploy both in your account.
  - https://github.com/tom5610/amazon-sagemaker-mlops-samples/blob/main/template.yaml
  
Move to the Readme.md file for Lab0 folder in the repo for further instructions.

Note:- For Lab0 and Lab1 we will be using the Cloud9 environment:
