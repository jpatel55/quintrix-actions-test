import json

def lambda_handler(event, context):
    print("Lambda received event:")
    print(json.dumps(event))

    # This just passes the S3 event details right through
    return event # comment added