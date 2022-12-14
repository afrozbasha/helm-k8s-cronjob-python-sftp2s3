import pysftp
import boto3

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

host = 's-c8cd657eb16040d48.server.transfer.ap-northeast-1.amazonaws.com'
port = 22
username = 'afroz'
privateKeyFilePath = 'id_rsa'

with pysftp.Connection(host=host, port=port, username=username, private_key=privateKeyFilePath, cnopts=cnopts) as sftp:
    print("connection established successfully")
    with sftp.cd('/a.f.r.o.z/afroz'):
        sftp.put('new_file.txt')
        print("file uploaded on bucket successfully")
        sftp.get('new_file.txt')
        print("file downloaded to local machine successfully")

s3_client = boto3.client('s3',
                         aws_access_key_id='AKIA***********CKQFV',
                         aws_secret_access_key='dDJcpyF2+*************lZt0v9GMcA',
                         region_name="ap-south-1")
file_name = 'new_file.txt'
bucket_name = 'from-sftp-data'
object_name = file_name

try:
    s3_client.upload_file(file_name, bucket_name, object_name)
    print('file:', file_name, ' uploaded on bucket:', bucket_name, ' successfully')
except Exception as e:
    print("failed to upload specified file")
    print(e)
