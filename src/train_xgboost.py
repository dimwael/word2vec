import boto3
import sagemaker
from sagemaker import get_execution_role

role = get_execution_role()

bucket = 'my-bucket' 
prefix = 'xgboost-model'

sess = sagemaker.Session()

xgb = sagemaker.estimator.Estimator(
    'xgboost',
    role,
    train_instance_count=1, 
    train_instance_type='ml.m4.xlarge',
    output_path=f's3://{bucket}/{prefix}/output',
    sagemaker_join_source_uri='s3://{bucket}/{prefix}/code/source.py')

xgb.set_hyperparameters(
    max_depth=5,
    eta=0.2,
    gamma=4,
    min_child_weight=6,
    subsample=0.8,
    objective='binary:logistic',
    num_round=100)

s3_input_train = sagemaker.s3_input(s3_data='s3://{}/{}/train'.format(bucket, prefix), content_type='csv')
s3_input_validation = sagemaker.s3_input(s3_data='s3://{}/{}/validation'.format(bucket, prefix), content_type='csv')

xgb.fit({'train': s3_input_train, 'validation': s3_input_validation})