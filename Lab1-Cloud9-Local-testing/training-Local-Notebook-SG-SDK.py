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


## Note the below 3 lines are only for local mode
from sagemaker.local import LocalSession
sagemaker_session = LocalSession()
sagemaker_session.config = {'local': {'local_code': True}}


# In[7]:


bucket_name = "XXXXXX"
model_dir = "s3://XXXXXX/training-output"


# In[8]:


train_data = "s3://XXXXXX/DataProcessed/train/X_train/" 
train_label = "s3://XXXXXX/DataProcessed/train/y_train/"
val_data =         ----------------------------------------------------------- To be Filled ---------------------------------------------------------

val_label =         ----------------------------------------------------------- To be Filled ---------------------------------------------------------

test_data =         ----------------------------------------------------------- To be Filled ---------------------------------------------------------


inputs = {
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

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



# In[12]:


estimator = TensorFlow(
    entry_point="main.py",
    source_dir="script_train",
    instance_type='local',
    instance_count=1,
    hyperparameters=hyperparameters,
    role=sagemaker.get_execution_role(),  # Passes to the container the AWS role that you are using on this notebook
    framework_version="XXXX",
    py_version="XXXXX",
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

)


# In[13]:


estimator.fit(inputs)


# In[ ]:





# In[ ]:




