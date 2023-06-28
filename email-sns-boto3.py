import boto3
mysns = boto3.client("sns")
    
def lambda_handler(event, context):
    mysns.publish(
        TopicArn=" your topic arn",
        Message="Something uploaded",
        Subject="New doc in s3"
        )
    print("hello i am vsr from s3 .....calling sns")
