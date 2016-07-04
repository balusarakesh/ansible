import boto3
import time
import datetime

client = boto3.client('cloudwatch', aws_secret_access_key='', aws_access_key_id='', region_name='us-west-1')


def get_cpuutilization():
    response = client.get_metric_statistics(
        Namespace = 'AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-092bca1b055fec17d'
            },
        ],
        StartTime=datetime.datetime.now()-datetime.timedelta(seconds=300),
        EndTime=datetime.datetime.now() ,
        Period=60,
        Statistics=[
            'Maximum',
        ],
    Unit='Percent'                                
    
    )
    percentages = []
    for each in response['Datapoints']:
        percentages.append(float(each['Maximum']))
    return max(percentages)
while True:
    client2 = boto3.client('ses', aws_secret_access_key='', aws_access_key_id='', region_name='us-east-1')
    percentage = get_cpuutilization()
    if percentage > 95:
        client2.send_email(Source='rakesh8015@gmail.com',
            Destination={
                'ToAddresses': [
                    'rakesh4ru@gmail.com',
                ]
            },
            Message={
                'Subject': {
                    'Data': 'Hi from AWS'
                },
                'Body': {
                    'Text': {
                        'Data': 'Your CPUUtilization is ' + str(percentage)
                    }
                }
            }
        )
    time.sleep(5*1000*60)
