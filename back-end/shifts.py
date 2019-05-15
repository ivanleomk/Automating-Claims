from datetime import timedelta
from datetime import datetime

def generateShifts(shifts):
    compiled_shifts = {}
    for i in shifts.keys():
        starting_time = shifts[i][0][0]
        starting_time_obj = datetime.strptime(starting_time,"%H:%M")
        total_hours = datetime.strptime("00:00","%H:%M")
        for j in range(len(shifts[i])):
            shift_start = datetime.strptime(shifts[i][j][0],"%H:%M")
            shift_end = datetime.strptime(shifts[i][j][1],"%H:%M")
            time_difference = shift_end-shift_start
            total_hours+=time_difference;

        ending_time = shifts[i][j][1]
        ending_time_obj = datetime.strptime(ending_time,"%H:%M")
        total = ending_time_obj - starting_time_obj
        converted_hours = total_hours - datetime(1900, 1, 1)
        difference = total - converted_hours
        compiled_shifts[i] = [str(starting_time),str(ending_time),str(difference),str(total_hours)[-8:]]
        #     # TODO: Figure out how to sum up the total number of hours worked
        # print(total_hours)
    return compiled_shifts;
