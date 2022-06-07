#!/usr/bin/env python
# coding: utf-8

# In[419]:


import numpy as np
from datetime import datetime


# In[420]:


facilities={1:'Club House',2:'Tennis Court'}


# In[ ]:





# In[488]:


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


# In[489]:


#combining the values from the arrays 
def Combiner(date,time,facility):
    combine=" "
    combine=combine+" "+facility+" "+date+" "+time
    return combine


# In[490]:


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


# In[491]:


def SplitTime(Time):
    
    t2 = Time.split(":")
    t2 = int(t2[0])
    return t2


# In[496]:


j=1
for i in range(len(final_arr)-1):
    print(final_arr[i])
    for j in range(1,len(final_arr)):
        print(final_arr[j].split(" "))


# In[ ]:





# In[526]:


def checktime(final_arr):
    j=1
    i=0

    for i in range(len(final_arr)-1):
        l1=[]
        l1=final_arr[i].split(" ")
        for j in range(1,len(final_arr)):
            l2=[]
            l2=final_arr[j].split(" ")
            if(l2[1]==l1[1] and l2[4]==l1[4]):
               
                T1_start=SplitTime(l1[-5])
                T2_start=SplitTime(l2[-5])
                T1_end = SplitTime(l1[-2])
                T2_end =SplitTime(l2[-2])
                
                if(T2_start<=T1_start or T2_start>T1_start):
                    if(T2_end<=T1_end):
                        return False
                        break
                    else: 
                        return True 


# In[ ]:





# In[541]:


#initializing the required arrays 
#this code should be run before the loop at every run 
time=[]
fac=[]
date=[]
final_arr=[]


# In[542]:


#Value to check the while loop
check=True


# In[543]:


#check expression to keep track of updates to each array 
count=0


# In[544]:


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
    #print(time[count])#,facilities[count]
    final_arr.append(Combiner(date[count],time[count],fac[count]))
    
    if(count>=1):
        tv=checktime(final_arr)
        
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


# In[545]:


fac=[]


# In[ ]:





# In[ ]:




