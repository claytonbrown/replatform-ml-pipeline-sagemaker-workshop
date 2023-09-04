#!/usr/bin/env python
# coding: utf-8

# In[2]:


## https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage.html


# In[3]:


from sagemaker.tensorflow import TensorFlow


# In[4]:


train_instance_type = "ml.m5.xlarge"


# In[5]:


import os

import sagemaker
from sagemaker.tensorflow import TensorFlow


# In[6]:


from sagemaker.inputs import TrainingInput
from sagemaker.workflow.steps import TrainingStep

from sagemaker.local import LocalSession
sagemaker_session = LocalSession()
sagemaker_session.config = {'local': {'local_code': True}}


# In[7]:


bucket_name = "techsummit2023mlops"
model_dir = "s3://techsummit2023mlops/training-output"


# In[8]:


train_data = "s3://techsummit2023mlops/DataProcessed/train/X_train/" 
train_label = "s3://techsummit2023mlops/DataProcessed/train/y_train/"
val_data = "s3://techsummit2023mlops/DataProcessed/val/X_val/"
val_label = "s3://techsummit2023mlops/DataProcessed/val/y_val/"
test_data = "s3://techsummit2023mlops/DataProcessed/test/"

inputs = {
            'train_output_data': train_data,
            'train_output_label': train_label,
            'val_output_data': val_data, 
            'val_output_label': val_label,
            'test_data': test_data
        }


# In[9]:


base_job_name="trainingJob"
checkpoint_in_bucket="checkpoints"

# The S3 URI to store the checkpoints
checkpoint_s3_bucket="s3://{}/{}/{}".format(bucket_name, base_job_name, checkpoint_in_bucket)

# The local path where the model will save its checkpoints in the training container
checkpoint_local_path="/opt/ml/checkpoints"


# In[10]:


hyperparameters={
    "output_dir": "/opt/ml/model",
    "bucket_name": bucket_name,
    "model_dir": model_dir
    }



# In[11]:


# We have to change the training.py to use python argument parser to receive these hyperparameters being passed.  Remove the line in training.py - "bucket_name = techsummit2023mlops"

# add below
# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument('--bucket_name', type=str, default="techsummit2023mlops")



# In[12]:


estimator = TensorFlow(
    entry_point="main.py",
    source_dir="script_train",
    instance_type='local',
    instance_count=1,
    hyperparameters=hyperparameters,
    role=sagemaker.get_execution_role(),  # Passes to the container the AWS role that you are using on this notebook
    framework_version="2.11.0",
    py_version="py39",
    checkpoint_s3_uri=checkpoint_s3_bucket,       ## https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints.html
    checkpoint_local_path=checkpoint_local_path, ## https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints.html
    output_path=model_dir    ## defines the S3 path to save the model and outputs
)


# In[13]:


estimator.fit(inputs)


# In[ ]:





# In[ ]:




