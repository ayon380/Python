#!/usr/bin/env python
# coding: utf-8

# In[1]:


## access characters from a string 
a="python"
## using index position
## +ve index strarst at 0
print(a[0])
print(len(a)) ## it is used for length of string


# In[2]:


## language ->a,e,l
##school->s,h,l
##learning->l,g,n
a="language"
print(a[1])
print(a[7])
print(a[0])


# In[3]:


a="school"
print(a[0])
print(a[2])
print(a[5])


# In[4]:


a="learning"
print(a[0])
print(a[7])
print(a[4])


# In[5]:


## negative index position
## -1 and ends at -length of string
a="python"
print(a[-1])
print(a[-6])


# In[6]:


## technology ->g,y
##powerful->p,w,r,l
## trending ->t,d,n,g
a="technology"
print(a[-2])
print(a[-1])


# In[7]:


a="trending"
print(a[-8])
print(a[-4])
print(a[-2])
print(a[-1])


# In[8]:


a="powerful"
print(a[-8])
print(a[-6])
print(a[-4])
print(a[-1])


# In[9]:


## accesssing substrings from given string 
a="python"
## pyt
## index slicing or string slicing
print(a[0:3])
print(a[-6:-3])


# In[10]:


b="colleage"
print(b[5:])
print(b[-3:])


# In[11]:


## string->str
## language->ang
## perform->form
a="string"
print(a[0:3])


# In[12]:


a="language"
print(a[1:4])


# In[13]:


a="perform"
print(a[3:])


# In[14]:


a="programme"
print(a[0::2]) ## skip one one element


# In[15]:


### take a string and reverse the string
b="python"
print(b[-1::-1])


# In[16]:


## string builtin  method
dir(str)


# In[17]:


## count()
a="pythonprogramme"
print(a.count("p"))


# In[18]:


## index()
a="language"
print(a.index("g"))


# In[19]:


##split()
a="pyt   hon"
a=a.split()
print(a)




# In[20]:


a="python"
a=a.split('t')
print(a)


# In[21]:


## join()
a="paytm"
a='@'.join(a)
print(a)


# In[22]:


## strip()
a="     python   "
print(a)
print(a.strip())


# In[23]:


## upper()
a="performance"
print(a.upper())


# In[24]:


## isupper()
a="perform"
print(a.isupper())


# In[ ]:




