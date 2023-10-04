import sys
import boto3

if len(sys.argv) != 3:
    print("Usage: python delete_file.py <bucket_name> <s3_object_name>")
    sys.exit(1)

bucket_name = sys.argv[1]
s3_object_name = sys.argv[2]

s3_client = boto3.client('s3', region_name='eu-west-1')

s3_client.delete_object(Bucket=bucket_name, Key=s3_object_name)