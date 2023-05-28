# myproject/urls.py
from django.urls import path
from myapp.views import GoogleCalendarInitView, GoogleCalendarRedirectView

urlpatterns = [
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view(), name='google_permission'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view(), name='google_redirect'),
    # Other URLs in your project
]
