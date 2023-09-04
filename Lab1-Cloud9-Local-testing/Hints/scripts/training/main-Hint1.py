from training import create_cnn_model, train_model
import argparse
import os
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--bucket_name', type=str, default="techsummit2023mlops")
parser.add_argument('--output_dir', type=str, default="/opt/ml/model")
parser.add_argument('--train_output_data', type=str, default=os.environ.get('SM_CHANNEL_TRAIN_OUTPUT_DATA'))
parser.add_argument('--train_output_label', type=str, default=os.environ.get('SM_CHANNEL_TRAIN_OUTPUT_LABEL'))
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

parser.add_argument('--test_data', type=str, default=os.environ.get('SM_CHANNEL_TEST_DATA'))
# parser.add_argument('--checkpoint_local_path', type=str, default="/opt/ml/checkpoints")


args, _ = parser.parse_known_args()

bucket_name = args.bucket_name
output_dir = args.output_dir
# train_data = args.train_data
# val_data = args.val_data

train_output_data = args.train_output_data
train_output_label = args.train_output_label
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

test_data =  args.test_data
# checkpoint_local_path = args.checkpoint_local_path

# print(bucket_name,output_dir,train_output_data, train_output_label,val_output_data, val_output_label )

    ######################################
    #             Load Data for Training #
    ######################################     
def main():
    X_train = np.load(train_output_data + '/X_train.npy')
    y_train = np.load(train_output_label + '/y_train.npy')
        ----------------------------------------------------------- To be Filled ---------------------------------------------------------

    
    # print(X_train,y_train,X_val, y_val )
    model = create_cnn_model()
    train_model(model, X_train, y_train, X_val, y_val, output_dir, bucket_name)
    
if __name__ == "__main__":
    main()
    
    