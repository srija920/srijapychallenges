s=eval(input())
r=[]
f=[]
for i in range(0,s):
    t=eval(input("number "+str(i+1)+":"))
    r.append(t)
for i in range(0,s):
    d=input("string "+str(i+1)+":")
    f.append(d)
for i in range(0,s):
    if((r[i]==len(f[i]))and(r[i]!=i+1)):
        f[i]=f[i].upper()
    else:
        f[i]=f[i].lower()


f=sorted(f,reverse=True)
for i in f:
    print(i)
    



        
        
        
    

    
        


            

            
        
    
       
    
    
    


