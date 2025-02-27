hours = list(map(int,input().split()))
minutes = list(map(int,input().split()))

total_minutes = 0
for hour in hours:
    total_minutes += hour*60
for minute in minutes:
    total_minutes += minute

hour = total_minutes//60
minute = total_minutes % 60
print(f"{hour}h {minute}m")
