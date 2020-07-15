import datetime
import pickle
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from django.core.serializers.json import DjangoJSONEncoder

# import django
# from django.conf import settings
# from sls import sls_defaults

# settings.configure(default_settings=sls_defaults, DEBUG=True)
# django.setup()

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def calendar_setup():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        # with open('token.pickle', 'wb') as token:
        #     pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service

    

def read_calendar():
    service = calendar_setup()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    calendarId='882q1makp7mtkq9lvirmqd36ac@group.calendar.google.com'
    print('Getting the upcoming events')
    events_result = service.events().list(calendarId=calendarId, timeMin=now, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    return events

    # if not events:
    #     print('No upcoming events found.')
    # for event in events:
    #     # start = event['start'].get('dateTime', event['start'].get('date'))
    #     print(event['htmlLink'], event['summary'], event['location'], event['start'].get('dateTime', event['start'].get('date')), event['end'].get('dateTime', event['start'].get('date')))


def create_event(program_instance):
    start_time = json.dumps(program_instance.start_time, cls=DjangoJSONEncoder)
    end_time = json.dumps(program_instance.end_time, cls=DjangoJSONEncoder)
    event ={
            'summary':program_instance.name,
            'location':program_instance.venue,
            'description': f'Speaker: {program_instance.speaker}\n{program_instance.description}',
            'start':{
                'dateTime':start_time.strip('"\''),
                'timeZone':'Africa/Nairobi',
                },
                'end':{
                    'dateTime':end_time.strip('"\''),
                    'timeZone':'Africa/Nairobi',
                    },
                }
    service = calendar_setup()
    calendarId='882q1makp7mtkq9lvirmqd36ac@group.calendar.google.com'
    event = service.events().insert(calendarId=calendarId, body=event).execute()
    program_instance.google_event_id = event['id']
    program_instance.save()


def update_event(program_instance, event_id):
    calendarId='882q1makp7mtkq9lvirmqd36ac@group.calendar.google.com'
    service = calendar_setup()
    try:
        current_event = service.events().get(calendarId = calendarId, eventId=event_id).execute()
        start_time = json.dumps(program_instance.start_time, cls=DjangoJSONEncoder)
        end_time = json.dumps(program_instance.end_time, cls=DjangoJSONEncoder)
        event ={
            'summary':program_instance.name,
            'location':program_instance.venue,
            'description': f'Speaker: {program_instance.speaker}\n{program_instance.description}',
            'start':{
                'dateTime':start_time.strip('"\''),
                'timeZone':'Africa/Nairobi',
                },
                'end':{
                    'dateTime':end_time.strip('"\''),
                    'timeZone':'Africa/Nairobi',
                    },
                }
        updated_event = service.events().update(calendarId=calendarId, eventId=current_event['id'], body=event).execute()
    except Exception as e:
        print('Error: ',e)
