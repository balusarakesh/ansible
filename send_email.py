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


def get_memory():
    data = os.popen("df -h").read()
    lines = data.split("\n")
    total = 0.0
    for line in lines[1:]:
        if line:
            total = total + float(re.findall('[^\s]+', line)[4].replace('%', ''))
    return total


while True:
    client2 = boto3.client('ses', aws_secret_access_key='', aws_access_key_id='', region_name='us-east-1')
    percentage = get_cpuutilization()
    memory = get_memory()
    if percentage > 95:
        message = 'Your CPUUtilization is ' + str(percentage)
    elif memory > 90:
        message = 'Your system memory usage is ' + str(memory) + '%'
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
                    'Data': str(message)
                }
            }
        }
    )
    
    time.sleep(5*1000*60)
