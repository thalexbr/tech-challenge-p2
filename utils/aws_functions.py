import boto3

sts_client = boto3.client('sts')
response = sts_client.assume_role(
    RoleArn='arn:aws:iam::your_account_id:role/your_role_name',
    RoleSessionName='your_session_name'
)

credentials = response['Credentials']
client = boto3.client('s3',
                     aws_access_key_id=credentials['AccessKeyId'],
                     aws_secret_access_key=credentials['SecretAccessKey'],
                     aws_session_token=credentials['SessionToken'])