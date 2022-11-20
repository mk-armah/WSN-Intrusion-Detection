import logging
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

#for testing functionality
import os
from dotenv import load_dotenv
load_dotenv(".env")


class AWS:
    def __init__(self,aws_access_key,aws_secret_access_key,bucket):


        self.aws_access_key = aws_access_key
        self.aws_secret_access_key = aws_secret_access_key

    # s3 client intitial call/setup
        self.s3 = boto3.resource(
            service_name='s3',
            aws_access_key_id = self.aws_access_key,   
            aws_secret_access_key = self.aws_secret_access_key  
            )
                  
        self.bucket = self.s3.Bucket(bucket)

        # configure logs
        self.logging = logging.basicConfig(
            level=logging.INFO, filemode="a+",
            filename="aws-config.log",
            format='%(asctime)s >> %(levelname)s >> %(message)s'
        )

    def getObject(self,path_to_object):
        """Create an S3 bucket in  S3 default region (us-east-1).
        Args:
            param bucket_name: Bucket to create

        Return:
            True if bucket created, else False
        """
        # Create bucket
        try:
            self.bucket.download_file(path_to_object,Filename = "./")
        except ClientError as e:
            self.logging.error(e)
            print("Action Failed : Please refer to logs at aws-config.log")
            return False
        
        else:
            return True

    def putObject(self,file_name,object_name=None):
        """Upload a file to S3 
        Args:
            param file_name: File to upload
            param bucket: Bucket to upload to
            param object_name: S3 object name. If not specified then file_name is used
        Return:
            True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = os.path.basename(file_name)

        # Upload the file

        try:
            response = self.s3.upload_file(file_name,self.bucket, object_name)
        except ClientError as e:
            self.logging.error(e)
            return False
        else:
            return True
            

if __name__ == "__main__":


    ACCESS_KEY_ID = os.environ.get("ACCESS_KEY_ID")
    SECRET_ACCESS_KEY = os.environ.get("SECRET_ACCESS_KEY")
    s3 = AWS(ACCESS_KEY_ID,SECRET_ACCESS_KEY,"wsn-intrusion-detection")
    print(ACCESS_KEY_ID)
    print(SECRET_ACCESS_KEY)
    s3.getObject("models/adaboost.chael")
    
