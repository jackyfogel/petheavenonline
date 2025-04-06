import boto3
from botocore.exceptions import NoCredentialsError, ClientError

import os

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'us-west-2')

def upload_test_file():
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_S3_REGION_NAME
    )

    try:
        test_content = b"Hello from Render!"
        test_key = "test_upload.txt"

        response = s3.put_object(
            Bucket=AWS_STORAGE_BUCKET_NAME,
            Key=test_key,
            Body=test_content,
            ContentType='text/plain',
            ACL='public-read'
        )

        file_url = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com/{test_key}"
        print("✅ Upload successful!")
        print("📂 File URL:", file_url)

    except NoCredentialsError:
        print("❌ No credentials found. Check your env vars.")
    except ClientError as e:
        print("❌ AWS Client error:", e)
    except Exception as e:
        print("❌ General error:", e)

if __name__ == "__main__":
    upload_test_file()
