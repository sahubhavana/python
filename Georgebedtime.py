s=input()
t=input()
h1,m1=map(int,s.split(":"))
currenttime=h1*60+m1 
ht,mt=map(int,t.split(":"))
sleeptime=ht*60+mt 
bed_time=currenttime-sleeptime
if bed_time<0:
    bed_time=bed_time+1440 
hh=bed_time//60
mm=bed_time%60 

print(f"{hh:02d}:{mm:02d}")