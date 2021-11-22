import boto3 

ec2_client_paris = boto3.client('ec2' , region_name ="eu-west-3")
ec2_resource_paris = boto3.resource('ec2' , region_name="eu-west-3")

ec2_client_Frankfurt = boto3.client('ec2' , region_name ="eu-central-1")
ec2_resource_Frankfurt = boto3.resource('ec2' , region_name="eu-central-1")

instances_ids_paris = []
instances_ids_Frankfurt = []


reservations_paris = ec2_client_paris.describe_instances()['Reservations']
for res in reservations_paris:
    instances = res['Instances']
    #collect all ec2 ids into list > add tags for all at once
    for ins in instances:
        instances_ids_paris.append(ins['InstanceId'])

response = ec2_resource_paris.create_tags(
    Resources=instances_ids_paris,
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'Developement_Env'
        },
    ]
)    

reservations_Frankfurt = ec2_client_Frankfurt.describe_instances()['Reservations']
for res in reservations_Frankfurt:
    instances = res['Instances']
    #collect all ec2 ids into list > add tags for all at once
    for ins in instances:
        instances_ids_Frankfurt.append(ins['InstanceId'])

response = ec2_resource_Frankfurt.create_tags(
    Resources=instances_ids_Frankfurt,
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'Production_Env'
        },
    ]
)    

