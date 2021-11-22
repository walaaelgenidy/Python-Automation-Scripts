import boto3

EKS_client = boto3.client('eks' , region_name="us-east-2")

EKS_Custers = EKS_client.list_clusters()['clusters']
for cluster in EKS_Custers:
    response = EKS_client.describe_cluster(
        name='EKS_Cluster' 
        )
        
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_version = cluster_info['version']
    cluster_endpoint = cluster_info['endpoint']

    print(f"Cluster {cluster} status is {cluster_status} and it's version is {cluster_version} and has endpoint {cluster_endpoint}")

