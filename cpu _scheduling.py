#1.cpu scheduling:FIFO
n=int(input("Enter the no of processes: "))
p=[]
t=[]#1,2,3
s=[0]
for i in range(n):
    #pro=int(input("Enter the number of process: "))
    num=int(input("Enter the the time burst for the each process: "))
    t.append(num)
print(t)
#now, add the elmnt i+1
for j in range(0,len(t)):
    k=(t[j] + s[j])
    print(k)
    o=j+1
    s.append(k)
print(s)
avg_waiting_time=(sum(s)-s[-1])
print(avg_waiting_time/n)
avg_training_time=(sum(s)-s[0])
print(avg_training_time/n)
