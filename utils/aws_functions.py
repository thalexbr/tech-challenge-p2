import boto3
import os

def upload_to_s3(source,destination, bucket, path):

    client = boto3.client('s3')


    save_path =  f'{path}/{destination}'

    client.upload_file(source, bucket,save_path)