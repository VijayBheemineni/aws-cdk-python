from hook import handler

event = {
    'Records': [
        {
            'Sns': {
                'Message': 'Test Message'
            }
        }
    ]
}

handler(event,{})