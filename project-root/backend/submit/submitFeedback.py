import json
import boto3
import uuid  # To generate a unique ID

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('feedback')  # Replace 'feedback' with your table name

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])

        feedback_item = {
            'id': str(uuid.uuid4()),  # Auto-generate unique ID
            'course': data['course'],
            'faculty': data['faculty'],
            'voice': data['voice'],
            'behavior': data['behavior'],
            'response': data['response'],
            'rating': data['rating'],
            'comments': data['comments']
        }

        table.put_item(Item=feedback_item)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': 'Feedback submitted successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': str(e)})
        }
