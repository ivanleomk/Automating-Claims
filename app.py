#Import modules
from __future__ import division

import sys
sys.path.append('./back-end')
from back import getCalendarList;
from excel import generateExcel;
from shifts import generateShifts;
import pprint
import xlsxwriter
from datetime import timedelta
from datetime import datetime
from parameters import parameters


def main():
    #Generates List Of Shifts
    shifts  = getCalendarList(parameters.parameters[BOUND])[[parameters.parameters[NAME]];
    compiled_shifts = generateShifts(shifts)
    #We then generate the compiled shifts  dictionary that lists [ Starting_Time, Ending_time, Break_Time]
    print(compiled_shifts)

# TODO: figure out how to then pass this into the original dictionary...


main();
