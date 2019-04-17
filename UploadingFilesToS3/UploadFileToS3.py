import boto3

#Creates an S3 client.
s3_client = boto3.client('s3')

#Simple function that opens a file, reads it and returns its data.
def read_file():
    file = open('SomeText.txt', 'r')
    file_data = file.read()
    file.close()
    return file_data
    
print('The current file content is: ' + read_file())
   
#Simple function that replaces characters with new ones at a given position.  
def replace_at(data, key_word, pos):
    return data[:pos] + key_word + data[pos + len(key_word):]

#Replaces the content of the file and stores it in a variable
updated_file = replace_at(read_file(), '. Just added some text for some reason', 43)
print('The updated file content is now: ' + updated_file)

# Create an Amazon S3 Bucket
# The example below shows how to create a new bucket using create_bucket.
s3_client.create_bucket(Bucket='the-most-awesome-test-bucket', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
print('Yass, bucket created')

# Uploads the file to the Bucket
# In order to use the 'Bucket' attribute we need to create a resource of s3.
s3_resource = boto3.resource('s3')

# In this scenario we upload the files data as an object using put_object
# We asign the path we want for the file as a Key and the data of the file as the Body
bucket_name = 'the-most-awesome-test-bucket'
s3_resource.Bucket(bucket_name).put_object(Key='the-text-we-edited.txt', Body=updated_file)
print('Yas, file uploaded')

# Deletes the file 
s3_client.delete_object(Bucket='the-most-awesome-test-bucket', Key='the-text-we-edited.txt')
print('Yas, file deleted')

# Deletes the bucket
s3_client.delete_bucket(Bucket='the-most-awesome-test-bucket')
print('Yas, bucket deleted')
