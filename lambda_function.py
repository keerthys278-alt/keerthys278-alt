import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

INSTANCE_ID = os.environ.get("INSTANCE_ID")
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")

def lambda_handler(event, context):
    logger.info(f"Restarting EC2 instance {INSTANCE_ID}")

    ec2.reboot_instances(
        InstanceIds=[INSTANCE_ID]
    )

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message="EC2 restarted due to high latency alert",
        Subject="Latency Automation"
    )

    return {
        "status": "success"
    }
