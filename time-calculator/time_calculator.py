def get_time(time):
    # Split
    part=time.split(':')
    hour=int(part[0])
    minute=int(part[1])
    return [hour,minute]

def add_time(start, duration, day=''):
    # get AM, PM
    if ((start.split())[1]).upper()=='AM':
        is_am = True
    else:
        is_am = False
    # Variables
    start_time = get_time((start.split())[0])
    duration_time = get_time(duration)
    half_day=0
    xhour=0
    days=0


    # adding minute
    tminute=start_time[1] + duration_time[1]
    if tminute > 60:
        xhour= 1
        minute=str(tminute-60).rjust(2,"0")
    else:
        minute=str(tminute).rjust(2,"0")

    # adding hour
    thour=start_time[0] + duration_time[0] + xhour
    while thour>12:
        thour-=12
        half_day+=1
    if xhour==1 and thour%12==0:
        half_day+=1
    hour=str(thour)

    

    # day later?
    if half_day == 0 :
        days = 0
    elif half_day == 1:
        if is_am:
            days = 0
        else:
            days = 1
    elif half_day%2==0:
        days = half_day/2
    else: 
        if is_am:
            days = half_day/2
        else:
            days = half_day//2 + 1

    # AM/PM?
    if half_day%2==0:
        is_am = is_am
    else:
        is_am = not is_am
    if is_am:
        am = 'AM'
    else:
        am = 'PM'

    

    # formating new_time
    new_time = f'{hour}:{minute} {am}'

    # Day of the week
    if day != '':
        current_day = day.title()
        day_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = day_of_the_week.index(current_day) + days
        if day_index < 7:
            day_index = int(day_index)
        else:
            day_index = int(day_index%7)
        new_time = f'{new_time}, {day_of_the_week[day_index]}'  

    if days == 0:
        new_time = new_time
    elif days == 1:
        new_time = f'{new_time} (next day)'
    else:
        new_time = f'{new_time} ({days} days later)'

    return new_time