import json

def lambda_handler(event, context):
    message = json.dumps(event);  
    return { 
        'message' : message
    }  
