#Putting data in a List


import boto3

# AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
region_name = 'YOUR_REGION'

# Create an S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Specify the bucket name
bucket_name = 'your_bucket_name'

# List to store keys
keys_list = []

# List objects in the specified S3 bucket
response = s3_client.list_objects_v2(Bucket=bucket_name)

# Check if the bucket contains any objects
if 'Contents' in response:
    for obj in response['Contents']:
        # Append 'Key' attribute to the list
        keys_list.append(str(obj['Key']))

# Print the list of keys
print("List of Keys:")
print(keys_list)




#Storing data in DataFrame:

import boto3
import pandas as pd

# AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
region_name = 'YOUR_REGION'

# Create an S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Specify the bucket name
bucket_name = 'your_bucket_name'

# List to store keys
keys_list = []

# List objects in the specified S3 bucket
response = s3_client.list_objects_v2(Bucket=bucket_name)

# Check if the bucket contains any objects
if 'Contents' in response:
    for obj in response['Contents']:
        # Append 'Key' attribute to the list
        keys_list.append(str(obj['Key']))

# Create a DataFrame
df = pd.DataFrame(keys_list, columns=['Key'])

# Print the DataFrame
print("DataFrame:")
print(df)





#Reading the contents of the file with DataFrame:

import boto3
import pandas as pd

# AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
region_name = 'YOUR_REGION'

# Create an S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Specify the bucket name
bucket_name = 'your_bucket_name'

# List to store keys and contents
file_data = []

# List objects in the specified S3 bucket
response = s3_client.list_objects_v2(Bucket=bucket_name)

# Check if the bucket contains any objects
if 'Contents' in response:
    for obj in response['Contents']:
        # Get the object key
        obj_key = obj['Key']
        
        # Download the object
        response = s3_client.get_object(Bucket=bucket_name, Key=obj_key)
        
        # Read the content of the object
        content = response['Body'].read().decode('utf-8')
        
        # Append key and content to the list
        file_data.append({'Key': obj_key, 'Content': content})

# Create a DataFrame
df = pd.DataFrame(file_data)

# Print the DataFrame
print("DataFrame:")
print(df)







#Deleting the FIle from S3:


import boto3
import pandas as pd

# AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
region_name = 'YOUR_REGION'

# Create an S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Specify the bucket name
bucket_name = 'your_bucket_name'

# List to store keys and contents
file_data = []

# List objects in the specified S3 bucket
response = s3_client.list_objects_v2(Bucket=bucket_name)

# Check if the bucket contains any objects
if 'Contents' in response:
    for obj in response['Contents']:
        # Get the object key
        obj_key = obj['Key']
        
        # Download the object
        response = s3_client.get_object(Bucket=bucket_name, Key=obj_key)
        
        # Read the content of the object
        content = response['Body'].read().decode('utf-8')
        
        # Delete the object
        s3_client.delete_object(Bucket=bucket_name, Key=obj_key)
        
        # Append key and content to the list
        file_data.append({'Key': obj_key, 'Content': content})

# Create a DataFrame
df = pd.DataFrame(file_data)

# Print the DataFrame
print("DataFrame:")
print(df)







#Deleting a particular File:

import boto3

# AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
region_name = 'YOUR_REGION'

# Create an S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Specify the bucket name
bucket_name = 'your_bucket_name'

# Specify the prefix of the files you want to delete
file_prefix_to_delete = 'prefix_to_delete/'

# List objects in the specified S3 bucket with the specified prefix
response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=file_prefix_to_delete)

# Check if the bucket contains any objects with the specified prefix
if 'Contents' in response:
    for obj in response['Contents']:
        # Get the object key
        obj_key = obj['Key']
        
        # Delete the object
        s3_client.delete_object(Bucket=bucket_name, Key=obj_key)
        print(f"Deleted file: {obj_key}")
else:
    print("No files found with the specified prefix to delete.")






#Uploading the file in S3 bucket:

import boto3

# AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
region_name = 'YOUR_REGION'

# Create an S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Specify the bucket name
bucket_name = 'your_bucket_name'

# Specify the local file path
local_file_path = '/path/to/your/local/file.txt'

# Specify the key (object name) under which to store the file in the bucket
s3_key = 'folder/file.txt'  # Example: 'folder/file.txt'

# Upload the file to the S3 bucket
s3_client.upload_file(local_file_path, bucket_name, s3_key)

print(f"File '{local_file_path}' uploaded to '{bucket_name}' with key '{s3_key}'.")


