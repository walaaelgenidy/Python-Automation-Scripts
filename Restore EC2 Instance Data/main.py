import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2' , region_name='us-east-2')
ec2_resource = boto3.resource('ec2' , region_name='us-east-2')

instance_id = "i-03b81176574caeabc" 

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

instance_volume = volumes['Volumes'][0]

snapshots = ec2_client.describe_snapshots(
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume['VolumeId']]
        }
    ]
)

#restore only latest snapshot
latest_snapshot = sorted(snapshots['Snapshots'] , key=itemgetter('StartTime') , reverse=True)[0]

new_volume = ec2_client.create_volume(
    Encrypted=True,
    SnapshotId=latest_snapshot['SnapshotId'],
    AvailabilityZone="us-east-2",
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Prod'
                }
            ]
        }
    ]
)

while True:
    vol = ec2_resource.Volume(new_volume['VolumeId'])
    print(vol.state)

    if vol.state == 'available':
        ec2_resource.Instance(instance_id).attach_volume(
           Device='/dev/sda2',
           VolumeId = new_volume['VolumeId']
        )
        break
