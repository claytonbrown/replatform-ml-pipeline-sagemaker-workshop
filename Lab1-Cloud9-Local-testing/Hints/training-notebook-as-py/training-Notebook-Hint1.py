#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage.html


# In[ ]:


from sagemaker.tensorflow import TensorFlow


# In[ ]:


train_instance_type = "ml.m5.xlarge"


# In[ ]:


import os

import sagemaker
from sagemaker.tensorflow import TensorFlow


# In[ ]:


from sagemaker.inputs import TrainingInput
from sagemaker.workflow.steps import TrainingStep

from sagemaker.local import LocalSession
sagemaker_session = LocalSession()
sagemaker_session.config = {'local': {'local_code': True}}


# In[ ]:


bucket_name = "techsummit2023mlops"
model_dir = "s3://techsummit2023mlops/training-output"


# In[ ]:


train_data = "s3://techsummit2023mlops/DataProcessed/train/X_train/" 
train_label = "s3://techsummit2023mlops/DataProcessed/train/y_train/"
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------


inputs = {
            'train_output_data': train_data,
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

            'test_data': test_data
        }


# In[ ]:


base_job_name="trainingJob"
checkpoint_in_bucket="checkpoints"

# The S3 URI to store the checkpoints
checkpoint_s3_bucket="s3://{}/{}/{}".format(bucket_name, base_job_name, checkpoint_in_bucket)

# The local path where the model will save its checkpoints in the training container
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------


# In[ ]:


hyperparameters={
    "output_dir": "/opt/ml/model",
    "bucket_name": bucket_name,
    "model_dir": model_dir
    }



# In[ ]:


# We have to change the training.py to use python argument parser to receive these hyperparameters being passed.  Remove the line in training.py - "bucket_name = techsummit2023mlops"

# add below
# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument('--bucket_name', type=str, default="techsummit2023mlops")



# In[ ]:


estimator = TensorFlow(
    entry_point="main.py",
    source_dir="script_train",
    instance_type='local',
    instance_count=1,
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

    checkpoint_local_path=checkpoint_local_path, ## https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints.html
    output_path=model_dir    ## defines the S3 path to save the model and outputs
)


# In[ ]:


estimator.fit(inputs)


# In[ ]:





# In[ ]:




