import sys
import json
from oauth2client import client
from googleapiclient import sample_tools
from datetime import datetime
import pprint

#Declaring Global Variables
shifts = {}

def getCalendarList(month):
    return(main(sys.argv,month));

def main(argv,month):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar.readonly')

    try:
        page_token = None
        while True:
          #We initially call the Google API to get a list of all the events which have been created under the ERT shift
          events = service.events().list(calendarId="gq12914gcnt4hahr4l08u064r8@group.calendar.google.com", pageToken=page_token).execute()
          #We then loop each individual event
          for i in range(len(events["items"])):
              #We first extract the name of the person doing the shift
              person = str(events["items"][i]["summary"])
              #We then extract the date which the shift was performed on in MM-DD format
              date = events["items"][i]["start"]["dateTime"][5:10]
              #We then extract the month of the date in order to check if it matches the month of the date we are accessing
              eventmonth = date[0:2]
              #If it matches, we then proceed to further evaluate the month.
              if(int(eventmonth)==month):
                #We first grab the date of the object
                day = str(date[3:])
                #We then find the start of the shift
                start = str(events["items"][i]["start"]["dateTime"][11:16])
                #We then find the end of the shift
                end = str(events["items"][i]["end"]["dateTime"][11:16])
                #We then create an array that has the start and end of the shift in it.
                shift = [start,end]
                print(str(day)+":"+str(shift))
                #We then add this to the dictionary of shifts for the month;
                #If the person has done a shift before, we add the new array to the\\
                if person in shifts:
                    if day in shifts[person]:
                        shifts[person][day].append(shift)
                    else:
                        shifts[person][day] = [shift]
                else:
                    shifts[person] = {}
                    shifts[person][day] = [shift]
                print()
          return shifts;
          page_token = events.get('nextPageToken')

          if not page_token:
            break
    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')


# if __name__ == '__main__':
#     main(sys.argv)
