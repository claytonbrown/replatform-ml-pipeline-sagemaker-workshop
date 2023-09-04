                                        Welcome to the replatforming ML pipeline workshop. 

Hi There,

Welcome to this Workshop for replatforming ML pipeline to Sagemaker Pipelines

Github - https://github.com/sumirk/ml-replatform-pipeline-sagemaker-workshop/tree/main


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
  

Note:- For Lab0 and Lab1 we will be using the Cloud9 environment:



-------------------------Lab0 Cloud9 docker pipeline --------------------------------


For Lab0 and Lab1 we will be using the Cloud9 environment:


- Clone this repository in Cloud9 environment - git clone https://github.com/sumirk/ml-replatform-pipeline-sagemaker-workshop.git

- Change the current directory to "Lab0-cloud9-docker-pipeline/"

- Use the below commands to resize the EBS volume:-
    - chmod +x resize.sh
    - ./resize.sh 20
  - https://docs.aws.amazon.com/cloud9/latest/user-guide/move-environment.html


- Run the command "chmod +x deploy-cfn-run-task.sh" in the root diretory
  
- Run the bash script './deploy-cfn-run-task.sh' and then run pass the s3-bucket name, the stack-name and your AWS account number to this command. for eg - ./deploy-cfn-run-task techsummit2023mlops cfn-test-summit-cli-01 9707709xxxx
  
- The above step will create a cloudformation template and build the docker container from the DockerFile locally and tag and push the image to ECR.
  
- A Fargate ECS cluster will also be created which will run a task to run the ML pipeline project as a standlone task in your accounts default VPC, Default Subnet with Default security group.
  
- So, please validate if they provide network connectivity to connect to public resources.
  
- The trained model and the checkpoints will be saved to your S3 bucket by the container task and then the task will be stopped.
  
- The training metrics are being logged to Cloudwatch by the Fargate task. If you want to take a look check the tasks logging in ECS console.
  
- If you want to run the task again you can do so by running the "aws ecs run-task ...." command from the shell script.
  
- You should spend the initial 10-15 mins to understand this project and have taken note of the steps and resources being created.

- The below two diagrams/screenshots show the structure of the project.

![image](https://github.com/sumirk/ml-replatform-pipeline-workshop/assets/53355338/07ef5076-1ea8-45ab-a68e-a86a7555095e)


![image](https://github.com/sumirk/ml-replatform-pipeline-workshop/assets/53355338/c028f47a-4e45-4f24-9687-f2511275bbb9)


- After this step open Sagemaker Studio in other browser window if you already have Studio deployed and then use the system terminal to clone the below repository in your Sagemaker studio system terminal.

  - To open in browser - https://github.com/sumirk/ml-replatform-pipeline-sagemaker-workshop
  - Clone link - https://github.com/sumirk/ml-replatform-pipeline-sagemaker-workshop.git

- If you have completed the above steps - Congratulations !! you have completed the first section of this workshop. The fun begins now :)
  

Hop on to Lab0-cloud9-docker-pipeline folder and open the README.md file for further instructions.


