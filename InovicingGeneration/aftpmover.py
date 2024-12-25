import paramiko
import os

# Server and authentication details
hostname = 'your_hostname'
port = 22  # Default SFTP port
username = 'your_username'
password = 'your_password'
local_directory = 'C:/Users/yourname/Desktop/automation/'  # Directory with files to upload
remote_directory = '/your/remote/nas/path/'  # Remote directory path

# Initialize and configure SFTP client
try:
    # Establish SFTP connection
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Get the list of all files in the local directory
    files = os.listdir(local_directory)

    # Counter to generate file names like INV0001, INV0002, ...
    file_counter = 1

    # Upload each file
    for file_name in files:
        local_file_path = os.path.join(local_directory, file_name)  # Full path to local file

        # Ensure it's a file (not a directory)
        if os.path.isfile(local_file_path):
            # Create new file name with INV0001, INV0002, ...
            new_file_name = f"INV{file_counter:04d}{os.path.splitext(file_name)[-1]}"  # Maintain original extension
            remote_file_path = remote_directory + new_file_name  # Full path for remote file

            try:
                # Upload the file with the new name
                sftp.put(local_file_path, remote_file_path)
                print(f"Uploaded: {local_file_path} to {remote_file_path}")

                # Increment the file counter for next file
                file_counter += 1

            except Exception as e:
                print(f"Failed to upload {local_file_path}: {e}")

except Exception as e:
    print(f"Error during file upload: {e}")

finally:
    # Close connections
    if 'sftp' in locals():
        sftp.close()
    if 'transport' in locals():
        transport.close()
