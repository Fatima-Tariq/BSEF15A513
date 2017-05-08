#!usr/bin/env pytho n

processes={}
Exectime=[]
arrivaltime=[]
runningQueue=[]
ts=0
wt=0
tat=0
x=0

print "Enter time slice"
ts=input()
n=input("Enter total number of processes: ")
for i in range(0,n):
	print "Enter execution time of process :",i
        et=input()
        Exectime.append(et)
	print "Enter arrival timeof process ",i
	at=input()
	arrivaltime.append(at)
        processes[i+1]=[Exectime[i]]

for i in range (0,n):
	for j in range (0,n):
		if(arrivaltime[i]<arrivaltime[j]):
			temp=arrivaltime[i]
			arrivaltime[i]=arrivaltime[j]
			arrivaltime[j]=temp
			temp2=Exectime[i]
			Exectime[i]=Exectime[j]
			Exectime[j]=temp2
print "Process ID\tarrival time\tWaiting time"
for i in range(0,n):
	while(arrivaltime[x]<=wt):
		runningQueue.append(Exectime[x])
		x=x+1
        print i,"\t\t",arrivaltime[i],"\t\t",wt
        wt+=ts
	runningQueue[i]-=ts
