def count(item, time):
    count=0
    for i in time[(item + 1):]:
        if i != 0:
            count = count+1
    return count
            
def format_duration(sec):
    time = [0, 0, 0, 0, 0]
    time[4] = sec % 60
    time[3] = int(sec / 60) % 60
    time[2] = int(int(sec / 60) / 60) % 24
    time[1] = int(int(int(sec / 60) / 60) / 24)%365
    time[0] = int(int(int(int(sec /60) / 60) /24) /365)
    ans = ''
    for i in range(0,len(time)):
        m = ''
        if time[i] > 0:
            m = str(time[i])
            if i == 0:
                m = m + ' year' if time[i] == 1 else m + ' years'
            if i == 1:
                m = m + ' day' if time[i] == 1 else m + ' days'
            if i == 2:
                m = m + ' hour' if time[i] == 1 else m + ' hours'
            if i == 3:
                m = m + ' minute' if time[i] == 1 else m + ' minutes'
            if i == 4:
                m = m + ' second' if time[i] == 1 else m + ' seconds'
        if i != 4 and time[i]>0:
            c = count(i, time)
            if c > 0:
                m = m + ' and 'if c==1 else m + ', '
        ans = ans + m
    if sec == 0:
        return 'now'
    else:
        return ans
