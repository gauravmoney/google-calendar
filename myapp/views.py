# myapp/views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
from myproject.settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPES

def GoogleCalendarInitView(request):
    # Step 1: Start OAuth flow and prompt user for credentials
    flow = InstalledAppFlow.from_client_secrets_file(
        r'C:\Users\Gaurav\Downloads\task',
        scopes=SCOPES
    )
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    request.session['state'] = state  # Store state in session
    return HttpResponseRedirect(authorization_url)

def GoogleCalendarRedirectView(request):
    # Step 2: Handle redirect request and exchange code for access_token
    state = request.session.pop('state', None)
    flow = InstalledAppFlow.from_client_secrets_file(
        'path/to/client_secrets.json',
        scopes=SCOPES,
        state=state
    )
    flow.redirect_uri = request.build_absolute_uri(reverse('google-calendar-redirect'))
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credentials = flow.credentials

    # Get list of events in user's calendar using access_token
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
    events_result = service.events().list(calendarId='primary').execute()
    events = events_result.get('items', [])

    # Process events as needed
    # ...

    return HttpResponse("Calendar events fetched successfully!")
