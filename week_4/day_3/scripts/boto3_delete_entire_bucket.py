import sys
import boto3

if len(sys.argv) != 2:
    print("Usage: python delete_bucket.py <bucket_name>")
    sys.exit(1)

bucket_name = sys.argv[1]

region="eu-west-1"

s3_client = boto3.client('s3', region_name=region)

objects = s3_client.list_objects_v2(Bucket=bucket_name)

if 'Contents' in objects:
    for obj in objects['Contents']:
        s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])

s3_client.delete_bucket(Bucket=bucket_name)