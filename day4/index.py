
## Taken from stacked overflow
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def timestamp_compare(x, y):
    (t1, d1) = x
    (t2, d2) = y
    t1 = t1[1:-1].split(" ")
    t2 = t2[1:-1].split(" ")
    date1 = t1[0].split("-")
    date2 = t2[0].split("-")
    time1 = t1[1].split(":")
    time2 = t2[1].split(":")
    year1 = int(date1[0])
    year2 = int(date2[0])
    month1 = int(date1[1])
    month2 = int(date2[1])
    day1 = int(date1[2])
    day2 = int(date2[2])
    hour1 = int(time1[0])
    hour2 = int(time2[0])
    min1 = int(time1[1])
    min2 = int(time2[1])
    if (year1 == year2):
        if (month1 == month2):
            if (day1 == day2):
                if (hour1 == hour2):
                    if (min1 == min2):
                        return 0
                    else:
                        return min1 - min2
                else:
                    return hour1 - hour2
            else:
                return day1 - day2
        else:
            return month1 - month2
    else:
        return year1 - year2
    return 0

def get_guard_data():
    file = open('input.txt', 'r')
    unsorted = []
    for line in file.readlines():
        # decode the line
        line = line.splitlines()[0]

        # get the timestamp
        separatorIndex = line.find("]") + 1
        timestamp = line[0:separatorIndex]
        
        #get the rest of the info
        info = line[separatorIndex + 1:]
        
        #add the info to the list
        unsorted.append((timestamp, info))
    
    sorted_entries = sorted(unsorted, key=cmp_to_key(timestamp_compare))
    result = []
    guard = ""
    for (timestamp, entry) in sorted_entries:
        flag = entry[0]
        if flag == 'G':
            # this is a guard beginning entry
            entry = entry.split(" ")
            guard = entry[1]
        elif flag == 'w':
            time = timestamp[1:-1].split(":")[1]
            result.append((guard, 'wake', time))
            # this is a guard waking entry
        else:
            # this is a guard sleeping entry
            time = timestamp[1:-1].split(":")[1]
            result.append((guard, 'sleep', time))
    return result

def get_guard_dictionary(guard_data):
    guards = dict()
    i = 0
    while i < len(guard_data):
        (g_id, action, minute) = guard_data[i]
        if action != 'sleep': return None
        i += 1
        (g_id2, action2, minute2) = guard_data[i]
        if g_id != g_id2 or action == action2: return None
        if not g_id in guards:
            guards[g_id] = [0] * 60
        for j in range(int(minute), int(minute2)):
            guards[g_id][j] += 1
        i += 1
    return guards

def get_sleepiest_guard():
    guard_data = get_guard_data()
    guards = get_guard_dictionary(guard_data)
    max_seen = 0
    sleepiest_guard = ''
    for guard in guards:
        min_asleep = 0
        for i in guards[guard]:
            min_asleep += i
        if min_asleep == max_seen: print('something wrong')
        if min_asleep > max_seen:
            max_seen = min_asleep
            sleepiest_guard = guard
    sleepiest_minute = guards[sleepiest_guard].index(max(guards[sleepiest_guard]))
    return(sleepiest_guard, sleepiest_minute)

def freq_asleep_guard():
    guard_data = get_guard_data()
    guards = get_guard_dictionary(guard_data)
    most_asleep_guard = ''
    most_asleep_min = -1
    most_asleep_amt = 0
    for guard in guards:
        sleepiest_minute = guards[guard].index(max(guards[guard]))
        sleepiest_minute_amt = max(guards[guard])
        if sleepiest_minute_amt > most_asleep_amt:
            most_asleep_guard = guard
            most_asleep_min = sleepiest_minute
            most_asleep_amt = sleepiest_minute_amt
    return (most_asleep_guard, most_asleep_min, most_asleep_amt)


print(get_sleepiest_guard())
print(freq_asleep_guard())