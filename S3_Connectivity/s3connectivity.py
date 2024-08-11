# # Install Boto3: You've already done this, so you're good to go.

# # Set Up AWS Credentials:

# # Open the AWS Management Console and go to the IAM (Identity and Access Management) dashboard.
# # Create a new IAM user or use an existing one. It's recommended to create a new user with limited permissions for security purposes.
# # Attach policies to the user that grant the necessary permissions for the actions you want to perform. For example, if you want to interact with S3, attach the "AmazonS3FullAccess" policy. If you want more granular permissions, you can create custom policies.
# # Once the user is created, you'll get an Access Key ID and a Secret Access Key. Keep these credentials secure.
# # Configure your AWS CLI or SDK with these credentials. You can do this by running aws configure and providing the Access Key ID, Secret Access Key, default region, and output format (optional). Alternatively, you can set these credentials as environment variables (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY).
# press ctrl+/ to comment all selected lines

import boto3

# Initialize Boto3 with your AWS credentials
aws_access_key_id = 'your-access-key-id'
aws_secret_access_key = 'your-secret-access-key'
aws_region = 'your-aws-region'

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Now you can use the Boto3 resources and clients to interact with AWS services

s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
