------------------------------------------------ Lab3 - Pipeline ----------------------------------------------------------------------


If you have come this far, then this is really great!! 



Now you will not need to do any changes in the scripts. But rather just need to chain all the steps together and pass the outputs as inputs to the next steps.

Also, now you will be using Sagemaker Pipelines SDK which is an abstraction over the Sagemaker SDK. Most of the notebook deifnitions would remain same but just that the steps will be encapsulated by the pipeline SDK's.

Much of the pipeline is prepared for you with boiler plate code, but spend sometime to understand why they are there , particlary the way the paths have been setup.

Familiarize yourself with the pipelines SDK by going through below document. You only need to go through Processing, Training, Model, RegisterModel for this workshop.


https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html 

Go through these examples to understand how the inputs and outputs are linked between steps and get familiar to Sagemaker pipelines SDK


https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/train-register-deploy-pipeline-model/train%20register%20and%20deploy%20a%20pipeline%20model.ipynb

https://github.com/aws/amazon-sagemaker-examples/blob/89c54681b7e0f83ce137b34b879388cf5960af93/sagemaker-pipelines/tabular/abalone_build_train_deploy/sagemaker-pipelines-preprocess-train-evaluate-batch-transform.ipynb 

