import boto3 
import schedule

ec2_client = boto3.client('ec2' , region_name='us-east-2')
ec2_resource = boto3.resource('ec2' , region_name='us-east-2') #resource return an object , we can use for subsequent calls

def Check_health_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for  status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state} with status  {ins_status} and system status is {sys_status}")
#to get a live health check
schedule.every(5).seconds.do(Check_health_status)   

while True:
    schedule.run_pending()