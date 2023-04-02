# import json
def lambda_handler(event, context):
    # get sns message from event and load json object
    message = event['Records'][0]['Sns']['Message']
    # print message
    print(message)