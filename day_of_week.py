day = int(raw_input('Day (0-6)? '))

#$ python day_of_week.py
#Day (0-6)? 5
#Friday
#$ python day_of_week.py
#Day (0-6)? 0
#Sunday

if day == 0:
    print 'Sunday'
if day == 1:
    print 'Monday'
if day == 2:
    print 'Tuesday'
if day == 3:
    print 'Wednesday'
if day == 4:
    print 'Thursday'
if day == 5:
    print 'Friday'
if day == 6:
    print 'Saturday'