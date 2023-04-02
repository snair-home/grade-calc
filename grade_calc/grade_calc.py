import boto3
import json
import os

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    # get topic from environment variable
    topic = os.environ['GRADE_CALC_TOPIC']
    # get bucket name from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    # get file/key name
    key = event['Records'][0]['s3']['object']['key']
    # get file object
    response = s3.get_object(Bucket=bucket, Key=key)
    # read file content
    file_content = response['Body'].read().decode('utf-8')
    #  load json object
    scores = json.loads(file_content)

    # print content of each record
    for score in scores:
        # print(score)
        # if score is greater than 80, then Assign grade A else Assign grade B
        # [ERROR] TypeError: '>' not supported between instances of 'str' and 'int'
        # cast score to int
        score['score'] = int(score['score'])

        if score['score'] > 80:
            score['grade'] = 'A'
        else:
            score['grade'] = 'B'
        print(score)
        # publish message to SNS topic
        sns.publish(TopicArn=topic, Message=json.dumps({'default': json.dumps(score)}), 
                    MessageStructure='json')

