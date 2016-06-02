def tranHourtoMinute(strTime):
    nums = strTime.split(':')
    return int(nums[0])*60+int(nums[1])

def tranMinutetoHour(strTime):
    hour,minute = divmod(int(strTime),60)
    return '%d:%d'%(hour,minute)

if __name__=='__main__':
    while True:
        strTime = raw_input("Please enter the time,like 12:12,or enter 'q' to quit")
        if strTime.lower()=='q':
            break
        else:
            print 'the time is: %d minutes' % tranHourtoMinute(strTime)
            print 'the same time is: %s' % tranMinutetoHour(tranHourtoMinute(strTime))
