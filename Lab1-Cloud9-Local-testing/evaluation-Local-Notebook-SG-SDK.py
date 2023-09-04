#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[8]:


model_data = 's3://techsummit2023mlops'
test_data_eval = 's3://techsummit2023mlops/DataProcessed/test/'


# In[ ]:





# In[9]:


import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.sklearn.processing import SKLearnProcessor

region = boto3.session.Session().region_name

role = get_execution_role()
# sklearn_processor = SKLearnProcessor(
#     framework_version="0.20.0", role=role, instance_type="ml.m5.xlarge", instance_count=1
# )


## Note the below 3 lines are only for local mode
from sagemaker.local import LocalSession
sagemaker_session = LocalSession()
sagemaker_session.config = {'local': {'local_code': True}}


# In[10]:


from sagemaker.tensorflow import TensorFlowProcessor
from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker import get_execution_role

region = boto3.session.Session().region_name

role = get_execution_role()
BUCKET = 'XXXXXXXXXX'
eval_path = 'DataEvaluation/metrics/'

#Initialize the TensorFlowProcessor
tp = TensorFlowProcessor(
    framework_version='2.11.0',
    role=get_execution_role(),
    instance_type='local',
    instance_count=1,
    base_job_name='frameworkprocessor-TF',
    py_version='py39'
)

#Run the evaluation job
tp.run(
    code='evaluation.py',
    source_dir='script_evaluation',
    inputs=[
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

    ],
    outputs=[
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------
    ]
)

    


# In[ ]:




