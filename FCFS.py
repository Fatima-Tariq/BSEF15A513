#!usr/bin/env python

processes={}
Exectime=[]
wt=0
tat=0
awt=0
atat=0
n=input("Enter total number of processes: ")
for i in range(0,n):
	print "Enter execution time of process ",i
	et=input()
	Exectime.append(et)
	processes[i+1]=[Exectime[i]]

print "Process ID\t\tWaiting time\t\tTurn around time"
for i in range(0,n):
	tat=Exectime[i]+wt
	print i,"\t\t\t",wt,"\t\t\t",tat
	wt+=Exectime[i]
	awt+=wt
	atat+=tat
