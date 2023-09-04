#!/usr/bin/env python
# coding: utf-8

# In[2]:


import boto3
import sagemaker
from sagemaker import get_execution_role
region = boto3.session.Session().region_name

role = get_execution_role()


# In[5]:


source_data = "s3://XXXX/raw_data/"


# In[7]:


from sagemaker.tensorflow import TensorFlowProcessor
from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker import get_execution_role

region = boto3.session.Session().region_name

## Note the below 3 lines are only for local mode
from sagemaker.local import LocalSession
sagemaker_session = LocalSession()
sagemaker_session.config = {'local': {'local_code': True}}


role = get_execution_role()
BUCKET = 'XXXXXXX'
train_path = 'DataProcessed/train'
val_path = 'DataProcessed/val'
test_path = 'DataProcessed/test'

#Initialize the TensorFlowProcessor
tp = TensorFlowProcessor(
    framework_version='XXXX',
    role=get_execution_role(),
    instance_type='ml.m5.xlarge',
    instance_count=1,
    base_job_name='frameworkprocessor-TF',
    py_version='XXXX'
)

# there is a limit to the number of outputs to 10

#Run the processing job
tp.run(
    code='preprocessing.py',
    source_dir='script_processing',
    inputs=[
        ProcessingInput(input_name='XXXX',source=XXXX, destination="/opt/ml/processing/XXXX")
    ],
    outputs=[
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

        ProcessingOutput(output_name="test_data_eval", source="/opt/ml/processing/test", destination=f's3://{BUCKET}/{test_path}')
    ]
)


# In[ ]:





# In[ ]:




