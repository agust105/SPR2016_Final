monthstr = raw_input ("Enter a 3-letter abbrev. month:  ")
a = str (monthstr)

month_num = {'Jan':10, 'Feb':11, 'Mar':0, 'Apr':1, "May":2,
'Jun':3, 'Jul':4, 'Aug':5, 'Sept':6, 'Oct':7, 'Nov':8,
'Dec':9}

month = month_num[a]

yearstr = raw_input ("Enter a year:  ")
year = int (yearstr)

while year < 1600:
    yearstr = raw_input ("Must be a year after 1600 AD. Enter a year:  ")
    year = int (yearstr)

month_names = {'Jan':'January', 'Feb':'February', 'Mar':'March', 'Apr':'April', "May":'May',
'Jun':'June', 'Jul':'July', 'Aug':'August', 'Sept':'September', 'Oct':'October', 'Nov':'November',
'Dec':'December'}

print """
""", month_names[a], year
print """
Su  M  T  W  Th F  S"""

def leapyearsince(year):
    x = 0
    for pastyears in range(year-1600):
        if pastyears%400 == 0:
            x += 1
        elif pastyears%100 == 0:
            x += 0
        elif pastyears%4 == 0:
            x += 1
        else:
            x += 0
    return x

def februaryrule(year):
    if year%400 == 0:
        return 1
    elif year%100 == 0:
        return 0
    elif year%4 == 0:
        return 1
    else:
        return 0

def mon(month):
    if month == 11:
        return (28 + februaryrule(year))
    else:
        return (31 - ((month%5)%2))

# /n = new line

def days_months(month):
    if month == 11:
        return (month//5)*153 + ((month%5)*31)
    else:
        return (month//5)*153 + (month%5)*31 - ((month%5)//2)


if month >= 10:
    year -= 1
startday = ((year-1600)*365 + leapyearsince(year) + days_months(month)+ februaryrule(year) + 2)%7
year += 1


def cal_fill(month, startday):
    st = ""
    for i in range(startday):
        st += "   "
    for day in range(mon(month)):
        st += "%2d " %(day + 1)
        if (startday + day)%7 == 6:
            st += "\n"
    print st, "\n"



cal_fill(month, startday)
