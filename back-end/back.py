import sys
import json
from oauth2client import client
from googleapiclient import sample_tools
from datetime import datetime
import pprint

#Declaring Global Variables
shifts = {}

def getCalendarList():
    return(main(sys.argv,4));

def main(argv,month):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar.readonly')

    try:
        page_token = None
        while True:
          events = service.events().list(calendarId="gq12914gcnt4hahr4l08u064r8@group.calendar.google.com", pageToken=page_token).execute()
          for i in range(len(events["items"])):
              print(events["items"][i]["summary"])
              # person = events["items"][i]["summary"]
              # date = events["items"][i]["start"]["dateTime"][5:10]
              # #Filters out by Month:
              # eventmonth = date[0:2]
              # if(int(eventmonth)==month):
              #   day = date[3:]
              #   print(day)
              #   start = events["items"][i]["start"]["dateTime"][11:16]
              #   end = events["items"][i]["end"]["dateTime"][11:16]
              #   shift = [start,end]
              #   #Checks to see if that person has an existing
              #   if person in shifts:
              #       shifts[person][day] += [shift]
              #   else:
              #       shifts[person] = {};
              #       shifts[person][day] = [shift];
          return shifts;
          page_token = events.get('nextPageToken')

          if not page_token:
            break
    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')

print(getCalendarList());

# if __name__ == '__main__':
#     main(sys.argv)
