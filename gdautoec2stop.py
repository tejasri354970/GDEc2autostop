import boto3
import json
import os
def handler ('eve, context'):
try:
 ec2 = boto3.client('ec2')
instance ID = os.environ ['INSTANCE-ID']
response = ec2.stop-instances (
Instance Ids = [
  Instance ID,
],
except for client errors as e;
 print(e)
return response.
