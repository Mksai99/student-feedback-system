import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('admin_users')  # Table should exist with 'username' as Partition key

def lambda_handler(event, context):
    try:
        # Parse request body
        body = json.loads(event['body'])
        username = body.get('username')
        password = body.get('password')

        if not username or not password:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'success': False, 'message': 'Username and password required'})
            }

        # Fetch user from DynamoDB
        response = table.get_item(Key={'username': username})

        if 'Item' in response and response['Item']['password'] == password:
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'success': True, 'message': 'Login successful'})
            }
        else:
            return {
                'statusCode': 401,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'success': False, 'message': 'Invalid credentials'})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'success': False, 'message': str(e)})
        }
