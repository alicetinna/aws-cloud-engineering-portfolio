import base64
import json

def lambda_handler(event, context):
    print(f"🎬 Processing a batch of {len(event['Records'])} incoming streaming records...")
    
    for record in event['Records']:
        try:
            # 1. Decode the Kinesis Base64 payload
            base64_data = record['kinesis']['data']
            decoded_string = base64.b64decode(base64_data).decode('utf-8')
            click_event = json.loads(decoded_string)
            
            # 2. Enrich the record
            click_event['processed_by'] = 'AWS_Lambda_Worker'
            print(f"✅ Successfully Parsed Event: {click_event}")
            
        except Exception as e:
            print(f"❌ Error decoding individual record: {str(e)}")
            
    return {
        'statusCode': 200,
        'body': json.dumps('Batch processing complete!')
    }
