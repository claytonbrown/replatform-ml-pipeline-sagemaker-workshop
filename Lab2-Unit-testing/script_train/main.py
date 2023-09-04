from training import create_cnn_model, train_model
import argparse
import os
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--bucket_name', type=str, default="techsummit2023mlops")
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

# parser.add_argument('--checkpoint_local_path', type=str, default="/opt/ml/checkpoints")


args, _ = parser.parse_known_args()

bucket_name = args.bucket_name
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

# train_data = args.train_data
# val_data = args.val_data

        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

test_data =  args.test_data
# checkpoint_local_path = args.checkpoint_local_path

# print(bucket_name,output_dir,train_output_data, train_output_label,val_output_data, val_output_label )

    ######################################
    #             Load Data for Training #
    ######################################     
def main():
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

    
    # print(X_train,y_train,X_val, y_val )
    model = create_cnn_model()
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------
    
if __name__ == "__main__":
    main()
    
    