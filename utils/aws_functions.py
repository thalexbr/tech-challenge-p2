import boto3

def upload_to_s3(source,destination, bucket, path):

    client = boto3.client('s3')

    save_path =  f'{path}/{destination}'

    print(save_path)

    client.upload_file(source, bucket,save_path)