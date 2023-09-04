------------------------------------------------ Lab4 - Metrics ----------------------------------------------------------------------

Now we need to ensure that we can see the Training metrics in the Sagemaker

https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-experiments.html


If you are logging training metrics in your script in SystemOut then if you are using the built-in framework processors (Which we are using) then if you define the metric_definitions attribute in the training estimator, then Sagemaker Studio automatically integrates this with Sagemaker experiments and logs the metrics to the Dashboard for the experiment.


    metric_definitions=[
       {'Name': 'train:error', 'Regex': 'Train_error=(.*?);'},
       {'Name': 'validation:error', 'Regex': 'Valid_error=(.*?);'}
    ]
    
https://docs.aws.amazon.com/sagemaker/latest/dg/training-metrics.html#define-train-metrics




Also, we need to be able to see the evaluation metric in the Registry in Sagemaker Studio. You have to ensure 

Validate if you are able to see it. If not then try to find whats the problem.


Hint - Your metric JSON output should be in the below schema as defined in the below guide:-

https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-metrics.html 

Also, the evaluation file s3 path should be correct when its being being passed oin the register model step.