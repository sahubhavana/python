n=int(input())
fullweek=n//7
rem=n%7
minDaysOff=2*fullweek+(max(0,rem-5))
maxdayoff=2*fullweek+(min(2,rem))
print(minDaysOff,maxdayoff)