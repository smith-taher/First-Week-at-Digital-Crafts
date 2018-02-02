day = int(raw_input('Day (0-6)? '))

#$ python work_or_sleep_in.py
#Day (0-6)? 5
#Go to work
#$ python work_or_sleep_in.py
#Day (0-6)? 6
#Sleep in


#if day == 0 or day == 6:
    #print 'Sleep in'
#if day > 0 and day < 6:
    #print 'Go to work'

if day == 0 or day == 6:
    print 'Sleep in'
else:
    print 'Go to work'

