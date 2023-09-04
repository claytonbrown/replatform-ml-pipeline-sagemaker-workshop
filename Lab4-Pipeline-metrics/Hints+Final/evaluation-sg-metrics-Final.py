import os
import json
import shutil
import tensorflow as tf
from tensorflow.keras.models import load_model
from training import create_cnn_model, train_model
# from preprocessing import preprocess_data
from utils import upload_to_s3, download_data_from_s3
import numpy as np
import tarfile

test_data_eval = '/opt/ml/processing/test_data_eval'
model_data = '/opt/ml/processing/model_data/model.tar.gz'

# bucket_name = os.environ.get('BUCKET_NAME') 
# bucket_name = 'techsummit2023mlops'
# local_folder = './app/data'
# output_dir = './checkpoints'
# local_folder = '/app/data'
# output_dir = '/checkpoints'
# remote_folder = "raw_data"

def evaluate_model(model, X_test, y_test):
    
    with tarfile.open(model_data) as tar:
        tar.extractall(path=".")
    
    model.load_weights('./best_checkpoint.h5')
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test accuracy: {accuracy:.4f}")

    # Changed it to follow https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-metrics.html#model-monitor-model-quality-metrics-multi
    # evaluation_metrics = {
    #     "test_accuracy": accuracy,
    #     "test_loss": loss
    # }

    evaluation_metrics = {
                              "multiclass_classification_metrics" : {
                                "test_accuracy" : {
                                  "value" : accuracy,
                                  "standard_deviation" : "NaN"
                                },
                                "test_loss" : {
                                  "value" : loss,
                                  "standard_deviation" : "NaN"
                                }
                              }
                            }
    # Save evaluation metrics as JSON
    metrics_file_path = "/opt/ml/processing/eval_output/evaluation_metrics.json"
    with open(metrics_file_path, "w") as metrics_file:
        json.dump(evaluation_metrics, metrics_file)

    ## We dont need the below upload to S3 as we have written to /opt/ml/processing/eval_output , which pushes data to S3 automatically.
    # Upload evaluation metrics JSON to S3
    # upload_to_s3(metrics_file_path, "evaluation_metrics.json", bucket_name)
    

def main():
    # local_folder = "data"  # Local folder to save downloaded data
    # bucket_name = "your-s3-bucket-name"
    # download_data_from_s3(bucket_name, remote_folder, local_folder)
    
    # X_train, X_val, y_train, y_val, X_test, y_test = preprocess_data(local_folder)
    
    X_test = np.load(test_data_eval + '/X_test.npy')
    y_test = np.load(test_data_eval + '/y_test.npy')
    
    model = create_cnn_model()
    # train_model(model, X_train, y_train, X_val, y_val, output_dir)
    
    evaluate_model(model, X_test, y_test)

    # Clean up local files

if __name__ == "__main__":
    main()
