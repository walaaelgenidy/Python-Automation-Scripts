#automate data backup of EC2 instances taking snapshots automatically everyday
import boto3
import schedule

ec2_client = boto3.client('ec2' , region_name='us-east-2')

def create_backup():
    volumes = ec2_client.describe_volumes(
        Filters=[
        {
            'Name': 'tag:ENV',
            'Values': ['Prod']
        }
    ]
    )
    for volume in volumes['Volumes']:
        new_snapshots = ec2_client.create_snapshot(
            Description='created snapshot',
            VolumeId = volume['VolumeId']
        
        )
    print(new_snapshots)
schedule.every(1).day.do(create_backup)   

while True:
    schedule.run_pending()    