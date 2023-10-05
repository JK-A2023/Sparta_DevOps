import sys
import boto3

if len(sys.argv) != 4:
    print("Usage: python upload_file.py <bucket_name> <file_name> <object_name>")
    sys.exit(1)

bucket_name = sys.argv[1]
file_name = sys.argv[2]
object_name = sys.argv[3]

region="eu-west-1"

s3_client = boto3.client('s3', region_name=region)

s3_client.upload_file(file_name, bucket_name, object_name)