import sys
import json
from oauth2client import client
from googleapiclient import sample_tools
from datetime import datetime
from datetime import timedelta
import pprint
import unittest

#Declaring Global Variables
shifts = {}

def getCalendarList(bound):
    return(main(sys.argv,bound));

def main(argv,bound):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar.readonly')

    try:
        page_token = None
        dateRange = generateRange(bound)
        begin = dateRange[0]
        ending = dateRange[1]
        while True:
          #We initially call the Google API to get a list of all the events which have been created under the ERT shift
          events = service.events().list(calendarId="gq12914gcnt4hahr4l08u064r8@group.calendar.google.com", pageToken=page_token).execute()
          #We then loop through each individual event

          for i in range(len(events["items"])):
              #We first extract the name of the person doing the shift
              person = str(events["items"][i]["summary"])
              #We then extract the date which the shift was performed on in MM-DD format
              date = events["items"][i]["start"]["dateTime"][0:10]
              #Date of the event is then converted to a datetime object to see if it falls within the range.
              dateobj = datetime.strptime(date,'%Y-%m-%d')
              #We then extract the month of the date in order to check if it matches the month of the date we are accessing
              eventmonth = date[0:2]
              #If it matches, we then proceed to further evaluate the month.
              if(begin<=dateobj<=ending):
                #We first grab the date of the object
                day = str(date[8:])
                #We then find the start of the shift
                start = str(events["items"][i]["start"]["dateTime"][11:16])
                #We then find the end of the shift
                end = str(events["items"][i]["end"]["dateTime"][11:16])
                #We then create an array that has the start and end of the shift in it.
                shift = [start,end]

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
          return {"shifts": shifts,"range":[begin,ending,dateRange[2]]}
          page_token = events.get('nextPageToken')

          if not page_token:
            break
    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')

# print(getCalendarList(4))



#This generates the range for which we will proceed to evaluate the events.
def generateRange(date):
    #We have a dictionary with the starting dates of all months in DD-MM formatting
    startingDate = {
            #March , #April #May    #June   #July   #August #Sept(9)#Oct(10)  #Nov   #Dec
    2017: ["27-02","27-03","01-05","29-05","26-06","31-07","28-08","25-09","30-10","27-11"],
            #Jan , #Feb , #March , #April   #May(5) #June   #July   #August #Sept(9)#Oct(10)  #Nov   #Dec
    2018: ["01-01","29-01","26-02","26-03","30-04","28-05", "25-06", "30-07","27-08","01-10","29-10","26-11"],
            #Jan , #Feb , #March , #April #May    #June     #July   #August #September #November #December
    2019: ["31-12","28-01","25-02","01-04","29-04","27-05","01-07","29-07"]
    }

    #We first declare a list with the number of days in each calendar month, starting from March
    calendarDays = [[28,35,28,28,35,28,28,35,28,35],
    [28,28,28,35,28,28,35,28,35,28,28,35],[28,28,35,28,28,35,28,28]]

    #We set the intitial date as the 1st of January 2019 and add dates following that based on the number of days in each calendar month
    startingdate = "2017-02-27"
    #We then convert it to a date-time object
    startdateobj = datetime.strptime(startingdate,"%Y-%m-%d")

    #We then calculate what are the dates for the calendar month that we want the RFP to be generated within.
    dateobj = datetime.strptime(date,"%Y-%m")
    #We therefore extract the year and date of the desired Calendar Month, storing it in the variables Year and Date
    year = int(dateobj.year)
    month = int(dateobj.month)
    #We then do some data validation to check that the user's range of values lie within our dictionary
    if(year>=2020 | year<=2016):
        print("Invalid Range!")
        return "Invalid"
    elif(year == 2017):
        if month>=3:
            month-=2;
        else:
            return "Invalid Range"


    if(year == 2019 and month == 1):
        start = datetime.strptime(str(2018)+ "-"+startingDate[year][month-1],'%Y-%d-%m')
    else:
        start = datetime.strptime(str(year)+ "-"+startingDate[year][month-1],'%Y-%d-%m')

    end = start + timedelta(days = calendarDays[year-2017][month-1]-1 )
    return [start,end,calendarDays[year-2017][month-1]]

#checkdate()
# if __name__ == '__main__':
#     main(sys.argv)
