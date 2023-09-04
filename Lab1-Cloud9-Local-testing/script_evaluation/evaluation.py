import os
import json
import shutil
import tensorflow as tf
from training import create_cnn_model, train_model
# from preprocessing import preprocess_data
from utils import upload_to_s3, download_data_from_s3
import numpy as np

        ----------------------------------------------------------- To be Filled ---------------------------------------------------------



def evaluate_model(model, X_test, y_test):
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test accuracy: {accuracy:.4f}")

    evaluation_metrics = {
        "test_accuracy": accuracy,
        "test_loss": loss
    }

    # Save evaluation metrics as JSON
    metrics_file_path = "------------------------------"
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
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

    
    model = create_cnn_model()
    # train_model(model, X_train, y_train, X_val, y_val, output_dir)
    
    evaluate_model(model, X_test, y_test)

    # Clean up local files

if __name__ == "__main__":
    main()
