import schedule
import time
import requests


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '5591986106617',
        'message': 'Hello world',
        "key": 'textbelt'
    })
    print(resp.json())

# schedule.every().day.at('06:00').do(send_message())

# {'success': False, 'error': 'Sorry, free SMS are disabled for this country due to abuse.'}