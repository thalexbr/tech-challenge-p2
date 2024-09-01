import boto3

def upload_to_s3(file, bucket, path):

    # sts_client = boto3.client('sts')
    # response = sts_client.assume_role(
    #     RoleArn='arn:aws:iam::338003274337:role/EC2forSSMRole',
    #     RoleSessionName='Upload_to_S3_Session'
    # )

    # credentials = response['Credentials']
    # client = boto3.client('s3',
    #                     aws_access_key_id=credentials['AccessKeyId'],
    #                     aws_secret_access_key=credentials['SecretAccessKey'],
    #                     aws_session_token=credentials['SessionToken'])

    client = boto3.client('s3')

    save_path =  f'{path}/{file}'

    print(save_path)

    client.upload_file(file, bucket,save_path)