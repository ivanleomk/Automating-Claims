days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

def formatRange(dates):
    #We first extract the calendar day of the range
    startingDay = days[dates[0].weekday()]
    endingDay = days[dates[1].weekday()]

    #We then extract the month of the Range
    startingMonth = months[dates[0].month-1]
    endingMonth = months[dates[1].month -1]

    #We then extract the date of the Range
    startingDate = dates[0].day
    endingDate = dates[1].day

    #Next comes the Year
    Year = dates[0].year

    start = startingDay +", "+ str(startingDate)+ " " +startingMonth+ " "+ str(Year)
    end = endingDay +", "+str(endingDate)+ " " +endingMonth+ " "+ str(Year)

    return(start,end,dates[2])
