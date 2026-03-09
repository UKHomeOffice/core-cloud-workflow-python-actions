def lambda_handler(event, context):
    """Example AWS Lambda handler function."""
    name = event.get('name', 'Everyone')
    return {
        'statusCode': 200,
        'body': f'Hello, {name}!'
    }
