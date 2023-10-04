import sys
import boto3

if len(sys.argv) != 4:
    print("Usage: python download_file.py <bucket_name> <s3_object_name> <local_file_path>")
    sys.exit(1)

bucket_name = sys.argv[1]
s3_object_name = sys.argv[2]
local_file_path = sys.argv[3]

s3_client = boto3.client('s3', region_name='eu-west-1')

s3_client.download_file(bucket_name, s3_object_name, local_file_path)
