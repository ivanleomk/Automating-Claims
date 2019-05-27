#Import modules
from __future__ import division

import sys
sys.path.append('./back-end')
from back import getCalendarList;
from excel import generateExcel;
from shifts import generateShifts;
from formatRange import formatRange;
import pprint
import xlsxwriter
from datetime import timedelta
from datetime import datetime
from parameters import parameters as p

def main():
    #Generates List Of Shifts
    bound = p["BOUND"]
    name = p["NAME"]
    data  = getCalendarList(bound)
    shifts = data["shifts"]["Faith"]
    range = data["range"]
    print(range)
    print(formatRange(range))

    # compiled_shifts = generateShifts(shifts)
    #We then generate the compiled shifts  dictionary that lists [ Starting_Time, Ending_time, Break_Time]


# TODO: figure out how to then pass this into the original dictionary...
main();
