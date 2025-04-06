
import os
import boto3
from botocore.exceptions import ClientError

print("🔍 Checking AWS S3 Environment Variables")
env_keys = [
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_STORAGE_BUCKET_NAME",
    "AWS_S3_REGION_NAME"
]

for key in env_keys:
    print(f"{key} = {os.environ.get(key)}")

print("\n📡 Attempting to upload test file to S3...")

bucket = os.environ.get("AWS_STORAGE_BUCKET_NAME")
region = os.environ.get("AWS_S3_REGION_NAME")
file_key = "blog_images/test_s3_script.txt"
file_content = b"Hello from the S3 test script!"

try:
    s3 = boto3.client(
        "s3",
        region_name=region,
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
    )

    s3.put_object(Bucket=bucket, Key=file_key, Body=file_content, ACL="public-read")
    print(f"✅ Successfully uploaded to s3://{bucket}/{file_key}")
    print(f"🌐 Public URL: https://{bucket}.s3.{region}.amazonaws.com/{file_key}")
except ClientError as e:
    print("❌ Upload failed:", e)
