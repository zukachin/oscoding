num=(int(input("no of process needed: ")))
val=[]
l=[] 
final=[]
wait=[0]
for i in range(num):
    g=(input("order and time: ").split())
    val.append(g)
f=sorted(val)
for j in f:
    for u in j:
        k=int(u)
        l.append(k)
print(l)
for m in range(1,len(l),2):
    h=l[m]
    final.append(h)
for mom in range(0,len(final)):
    jk=(final[mom] + wait[mom])
    wait.append(jk)
print("waiting time: ",round(sum(wait[:-2])/num))
print("turnaround: ",round(sum(wait[1:])/num))
    
    



