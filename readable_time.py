"""
take in seconds and return a readable format as HH:MN:SS like this 01:33:21
"""
import math
def make_readable(seconds):
    readable_time = ""
    secs = 0
    mins = 0
    hrs = 0

    if seconds > 0 and seconds < 360000:
        #if seconds are less than a minute
        if seconds < 60:
            secs = seconds
        #if secons are less than an hour
        if seconds >=60 and seconds < 3600:
            if not seconds%60:
                mins = seconds/60
            else:
                #decimal part is sec and interger part is min
                secs,mins = math.modf(seconds/60)
                secs = secs * 60
        #if more than an hour
        if seconds >=3600:
            if not seconds%3600:
                hrs = seconds/3600
            else:
                mins,hrs = math.modf(seconds/3600)
                hrs = int(hrs)
                secs,mins = math.modf(mins*60)
                mins = int(mins)
                secs = secs*60
    hrs = str(hrs)
    #1 to 01
    hrs = str(hrs).zfill(2)
    mins = int(mins)
    mins = str(mins).zfill(2)
    real_sec = str(secs-int(secs))[1:]
    real_sec = float(real_sec)
    if real_sec > 0.5:
        secs = math.ceil(secs)
    else:
        secs = math.floor(secs)
    secs = str(secs).zfill(2)
    readable_time = hrs+":"+mins+":"+secs
    return readable_time




print(make_readable(43200))