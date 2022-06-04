#!/usr/bin/env python
# coding: utf-8

# In[208]:


import numpy as np
from datetime import datetime


# In[209]:


facilities={1:'Club House',2:'Tennis Court'}


# In[222]:


#initializing the required arrays 
time=[]
fac=[]
date=[]
final_arr=[]


# In[223]:


#Value to check the while loop
check=True


# In[ ]:





# In[224]:


#function to check the rate for the booking 
def CheckRate(facility,Time):
    cost=0
    
    T=Time.split('-')
    
    T1=T[0]
    T1=T1.split(" ")
        
    T2=T[-1]
    T2=T2.split(" ")
    
    t1 = datetime.strptime(T1[0], "%H:%M")
    
    t2 = datetime.strptime(T2[1], "%H:%M")
    
    if(t1>t2):
        diff=t1-t2
    else:
        diff=t2-t1
    
    time=str(diff).split(":")
    
    if(facility==1):
        cost=100
        Total=cost*int(time[0])
    else:
        cost=50
        Total=cost*int(time[0])
    print("Your Total Cost is",Total)


# In[225]:


#combining the values from the arrays 
def Combiner(date,time,facility):
    combine=" "
    combine=combine+" "+facility+" "+date+" "+time
    return combine


# In[226]:


#checking for equality between the arrays
def checker(final_arr):
    j=1
    if(len(final_arr)>2):
        for i in range(len(final_arr)):
            for j in range(len(final_arr)-1):
                if(final_arr[i]==final_arr[j]):
                    return False
                else:
                    return True
    else:
        if(final_arr[0]==final_arr[-1]):
            return False
        else:
            return True


# In[227]:


#check expression to keep track of updates to each array 
count=0


# In[228]:


#While loop to carry out the booking process 
while(check==True):
    
    print('Press 1 for Club House, Press 2 for Tennis Court')
    f=int(input())
    fac.append(facilities[f])
    
    if(f==1):
        print('The Rate for the Club House is Rs 100 per hour')
    else:
        print('The Rate for the Tennis Court is Rs 50 per hour')
    
    print('Please Enter the time you want to book the facility for: Eg 10:00 AM - 16:00 PM')
    duration=input()
    time.append(duration)
    
    print('Please Enter the date you want to book the facility for')
    dt=str(input())
    date.append(dt)
    print(time[count])#,facilities[count]
    final_arr.append(Combiner(date[count],time[count],fac[count]))
    
    if(count>=1):
        tv=checker(final_arr)
        
        if(tv==False):
            print('Booking Failed')
            break
        else:
            print('Booking Successful, Payment will be displayed below')
        
    CheckRate(f,duration)
    
    print('Do you want to continue the booking process? Y/N')
    
    T=input()
    
    if(T=='Y'):
        check=True
        count+=1
    else:
        check=False


# In[ ]:


fac=[]


# In[ ]:




