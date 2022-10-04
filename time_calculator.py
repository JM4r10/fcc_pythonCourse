# add_time takes in two required parameters and one optional parameter:
# a start time in the 12-hour clock format (ending in AM or PM)
# a duration time that indicates the number of hours and minutes
# (optional) a starting day of the week, case insensitive
# The function should add the duration time to the start time and return the result.

def add_time(start, duration, startingday = None):
    starthour = int(start[:start.find(':')])
    startmin = int(start[start.find(':')+1:start.find(' ')])
    period = start[-2:]
    addhour = int(duration[:duration.find(':')])
    addmin = int(duration[-2:])

    finalmin = startmin + addmin
    if finalmin >= 60:
        finalmin -= 60
        starthour += 1
#completed_days stores how many 24-hour cycles are in the duration specified
    completed_days = int(addhour/24)
    addhour = addhour-(completed_days*24)
    finalhour = starthour + addhour
#After calculating the finalhour in the clock, check if its greater or equal than 12. If so, it means at least one 12-hour cycle was completed. Substract that first cycle from the total of hours (finalhour) divides it by 12 to obtain how many 12-hour cycles it completed (thats why I use int() after the first one. #Since the day period(AM/PM) must change every 12-hour cycle completed, if the modulus of the result divided by 2 is 0, it means the total hours completed an odd numbers #of 12-hours cycles and so the day period changes. If the number of cycles is even, or the finalhour idnt complete a single 12-hour cycle, it remains the same.
    if finalhour >= 12:
        if int((finalhour-12)/12)%2 == 0:
            if period == 'AM': newperiod = 'PM'
            else: newperiod = 'AM'
        else: newperiod = period
    else: newperiod = period

    days_of_week = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    if newperiod == 'AM' and finalhour >= 12: completed_days += 1
    if startingday != None:
        newday = days_of_week.index(startingday.casefold().capitalize()) + completed_days
        if newday < len(days_of_week): newday = days_of_week[newday]
        else:
            while newday >= len(days_of_week):
                newday -= len(days_of_week)
            newday = days_of_week[(newday)]
#Converts the result into a 12-hour clock format and determinates how many days have passed (if any).
    if finalhour > 24: finalhour -= 24
    elif finalhour > 12: finalhour -= 12

    if len(str(finalmin)) == 1: finalmin = '0'+str(finalmin)
    # if completed_days == 1: time_elapsed = '(next day)'
    # else: time_elapsed = '('+str(completed_days)+' days later)'
    time_elapsed = '(next day)' if completed_days == 1 else '('+str(completed_days)+' days later)'

    if startingday == None and completed_days == 0: new_time = str(finalhour)+':'+str(finalmin)+' '+newperiod
    elif startingday == None and completed_days > 0: new_time = str(finalhour)+':'+str(finalmin)+' '+newperiod+' '+time_elapsed
    elif startingday != None and completed_days == 0: new_time = str(finalhour)+':'+str(finalmin)+' '+newperiod+','+' '+newday
    else: new_time = str(finalhour)+':'+str(finalmin)+' '+newperiod+','+' '+newday+' '+time_elapsed

    return new_time

#TESTING
print(add_time("8:16 PM", "466:02", "tuesday"))
print(add_time("8:16 PM", "466:02"))
