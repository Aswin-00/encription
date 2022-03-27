import random  #only works for txt
f=open('.txt','r') #put the path of the file  here 
w=open('.txt','a') #put the path were u want to save the file
ent=["%","^","&","$","#","@","!"] 
for u in f:
    v=list(u)
    w.write("\n")
    for i in range(0,len(u)):
        if u[i]==" ":
            w.write('tan60')  #space are replace by tan60
        else:
            w.write(str(u[i])+ent[random.randint(0,(len(ent)-1))])


f.close()
w.close()
