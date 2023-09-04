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


# In[10]:


from sagemaker.tensorflow import TensorFlowProcessor
from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker import get_execution_role


from sagemaker.local import LocalSession
sagemaker_session = LocalSession()
sagemaker_session.config = {'local': {'local_code': True}}


region = boto3.session.Session().region_name

role = get_execution_role()
BUCKET = 'techsummit2023mlops'
eval_path = 'DataEvaluation/metrics/'

#Initialize the TensorFlowProcessor
tp = TensorFlowProcessor(
    framework_version='2.11.0',
    role=get_execution_role(),
    instance_type='ml.m5.xlarge',
    instance_count=1,
    base_job_name='frameworkprocessor-TF',
    py_version='py39'
)

#Run the evaluation job
tp.run(
    code='evaluation.py',
    source_dir='script_evaluation',
    inputs=[
        ProcessingInput(input_name='model_data',source=model_data, destination="/opt/ml/processing/model_data"), 
        ProcessingInput(input_name='test_data_eval',source=test_data_eval, destination="/opt/ml/processing/test_data_eval"),
    ],
    outputs=[
        ProcessingOutput(output_name="eval_output_data", source="/opt/ml/processing/eval_output", destination=f's3://{BUCKET}/{eval_path}'),
    ]
)

    


# In[ ]:




