# def lamdba function
def lambda_handler(event, context):
    # loop thru the records in the event
    for record in event['Records']:
        print(record['body'])
