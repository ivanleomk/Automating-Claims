import xlsxwriter
from datetime import timedelta
from datetime import datetime

def generateExcel():
    #Generates Excel Workbook and Sheet using xlsxwriter
    workbook = xlsxwriter.Workbook('RFP.xlsx')
    worksheet = workbook.add_worksheet()

    # #Sets Column Widths
    worksheet.set_column(0,0, 1.83*1.1)
    worksheet.set_column(1,1, 23.83*1.007)
    worksheet.set_column(2,2, 14.83*1.01)
    worksheet.set_column(3,3, 14*1.01)
    worksheet.set_column(4,4, 15.83*1.01)
    worksheet.set_column(5,5, 13*1.01)
    worksheet.set_column(6,6, 23.5)

    #Formatting Template
    #Creating Title
    merge_format = workbook.add_format({
        'bold': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 24})
    worksheet.merge_range('A1:G1', 'TIMESHEET FOR YALE-NUS STUDENT ASSOCIATES', merge_format)

    #Instructions Section
    bold = workbook.add_format({'bold': True})

    worksheet.write('A3', 'Instructions', bold)
    worksheet.write('A4', '1')
    worksheet.write('A5', '2')
    worksheet.write('A6', '3')
    worksheet.write('A7', '4')
    worksheet.write('A8', '5')

    worksheet.write("B4","All fields/columns highlighted in yellow MUST contain correctly entered information before the timesheet can be processed.")
    worksheet.write("B5","For instructions on filling in the timesheet, hover the mouse cursor over the cells with a red triangle in the top right corner.")
    worksheet.write("B6","Submit the timesheet for work done each month by the 1st working day of the following month, to your department contact point for SAP.")
    worksheet.write("B7","The timesheet must be accompanied by a completed, printed and signed (by you) Request for Payment (RFP) form.")
    worksheet.write("B8","Before printing: do a print preview to check if the timesheet fits on a full A4 page. If it doesn't, adjust the scale under Page Layout.")

    #Personal Details
    studentName = workbook.add_format()
    studentName.set_text_wrap()
    studentName.set_font_size(16)
    studentName.set_font_name('Calibri')
    studentName.set_border()
    studentName.set_bold()


    #Data-Fields
    dataFields = workbook.add_format()
    dataFields.set_text_wrap()
    dataFields.set_font_size(16)
    dataFields.set_font_name('Calibri')
    dataFields.set_bg_color("FFEA89")
    dataFields.set_border()



    #General Data Fields
    gdataFields = workbook.add_format()
    gdataFields.set_text_wrap()
    gdataFields.set_font_size(14)
    gdataFields.set_font_name('Calibri')
    gdataFields.set_bg_color("FFEA89")
    gdataFields.set_border()

    #Default Bolded + Borders
    misc = workbook.add_format();
    misc.set_border();
    misc.set_bold();


    #Creates cells for Student Name and Data-FIeld for it
    worksheet.merge_range('A9:B10',"STUDENT NAME\n(exactly as in your Student ID)",studentName)
    worksheet.merge_range('C9:D10',FULL_NAME,dataFields)


    worksheet.write("E9","Residency Status",misc)
    worksheet.write("E10","Student ID Number",misc)
    worksheet.merge_range('F9:G9',RESIDENCY_STATUS,gdataFields)
    worksheet.merge_range('F10:G10',STUDENT_ID,gdataFields)

    worksheet.set_row(9, 19)

    #Second Row of stuff
    worksheet.merge_range('A12:B12',"Claiming for which month?",misc)
    worksheet.merge_range('A13:B13',"Claim Start Date",misc)
    worksheet.merge_range('A14:B14',"Claim End Date",misc)
    worksheet.merge_range('A15:B15',"Days in the Claim Month",misc)

    dates = {"Jan":["31 Dec","27 Jan"],"Feb":["28 Jan",""]}

    worksheet.write("E12","Hourly Rate",misc)
    worksheet.write("E13","Total Hours",misc)
    worksheet.write("E14","Amount Payable",misc)
    worksheet.write("E15","WBS Number",misc)

    # TODO: Figure out how to then pass in this information to the excel sheetss
    #Saves Changes
    workbook.close()
