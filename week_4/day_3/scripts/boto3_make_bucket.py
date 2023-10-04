import boto3
import sys

if len(sys.argv) != 2:
    print("Usage: python create_bucket.py <bucket_name>")
    sys.exit(1)

bucket_name = sys.argv[1]

s3_client = boto3.client('s3', region_name="eu-west-1")

bucket_name = input("Enter your bucket name here: ")

s3_client.create_bucket(Bucket=bucket_name,
                        CreateBucketConfiguration={'LocationConstraint': "eu-west-1"})
    
